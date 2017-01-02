import json

board = [3,7,[9,11], "abc"]
f = open("te.txt","w")
json.dump(board,f)
f.close()


"""f = open("te.txt","r")
board = json.load(f)     # board is now [3,7,[9,11], "abc"]
f.close()
print(board[0:])
"""


