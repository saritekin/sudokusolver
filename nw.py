import json

row= [0] * 9
board = []
point = 0
ao = [1,2,3,4,5,6,7,8,9]


for i in range(9):
     board.append(row[:])

qbfile = open("te.txt", "r")


for aline in qbfile:
    values = aline.split()


for row in board:
    for number in row:
        if number == 0:
            point += 1
            print(".", end=" ")
        else:
            print(number, end=" ")

    print()




