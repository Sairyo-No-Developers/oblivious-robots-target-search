from functools import reduce
from uuid import uuid4
from Graph import *
from Algorithm import *
from names import get_first_name
from time import sleep
from threading import Lock

class Robot:
    def __init__(self, initPos, target):
        self.id = str(uuid4())
        self.name = str(get_first_name())
        self.pos = initPos
        self.target = target
        self.done = False
        self.whiteboardValues = None
        self.graph = None
        self.robots = None
        self.cycles = 0
        self.moves = []
    
    def checkIfJunction(self,P):
        return True if len(P.graph.edges(self.pos)) > 2 else False
        
    def lookNeighbours(self):
        edges = [{"id": x[1], "val": self.whiteboardValues[x[1]], "occupied": self.checkOccupied(x[1])} for x in self.graph.edges(self.pos)]
        return edges, {"id": self.pos, "val": self.whiteboardValues[self.pos]}
    
    def updateWhiteboardValue(self, val):
        self.whiteboardValues[self.pos] = val
    
    def move(self, toPos, val = None):
        self.moves.append(f"Moved from {self.pos}:{self.whiteboardValues[self.pos]} to {toPos}:{self.whiteboardValues[toPos]}")
        if val: self.updateWhiteboardValue(val)
        self.pos = toPos
        # print(f"{self.name} moved to {toPos}")         
            
    def cycle(self, lock, P):
        while True:
            if not P.start: continue
            if self.done:
                break
            self.cycles += 1
            self.whiteboardValues = P.whiteboardValues
            self.graph = P.graph
            self.robots = list(map(lambda x: x.pos, P.robots.values()))
            if len(P.graph.edges(self.pos)) > 2:
                moreThanTwoNeighboursCycle(self)
            elif len(P.graph.edges(self.pos)) == 2:
                twoNeighboursCycle(self)
            else:
                oneNeighbourCycle(self)
            lock.acquire()
            P.whiteboardValues = self.whiteboardValues
            lock.release()
            sleep(0.0001)
        print(f"Thread stopped : {self.name}")
            
            
    def checkOccupied(self,pos):
        return True if pos in self.robots else False