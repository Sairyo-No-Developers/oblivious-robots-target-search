import pickle

moves = pickle.load(open("Max Moves.txt", "rb"))
for i in moves:
    print(i)
len(moves)