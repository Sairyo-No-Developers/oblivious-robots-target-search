import pytest
from src.oblivious_robots_target_searching.Graph import Playground

noOfNodes = 100
noOfRobots = 20

def checkResult(result):
    if result[0] != noOfNodes: return False
    if result[1] != noOfRobots: return False
    if result[2] < 10 or result[2] > 100: return False
    return True

def test_simRingWithChords():
    P = Playground(True)
    P.setup({
        "type": "ring-with-chords",
        "val": noOfNodes,
        "noOfRobots": noOfRobots,
        "noOfChords": 15
    })
    assert checkResult(P.run())