row = [0] * 9
board = []
point = 0
for i in range(9):
    board.append(row[0:])

# the game
board[0][1] = 2
board[0][3] = 6
board[0][5] = 5
board[1][4] = 3
board[1][6] = 6
board[1][7] = 1
board[2][0] = 7
board[2][2] = 6
board[2][6] = 3
board[3][1] = 5
board[3][3] = 2
board[3][4] = 8
board[3][6] = 1
board[3][7] = 4
board[4][1] = 4
board[4][2] = 7
board[4][5] = 3
board[4][8] = 8
board[5][6] = 9
board[5][7] = 6
board[6][4] = 9
board[6][5] = 1
board[7][1] = 7
board[7][2] = 9
board[7][6] = 4
board[7][7] = 2
board[7][8] = 1
board[8][2] = 1
board[8][3] = 4
board[8][4] = 7
board[8][5] = 2
board[8][6] = 8
board[8][7] = 3
board[8][8] = 9


def check0(x,y):
    arr = []
    cor = board[x][y]
    # seperate big cells
    if 0<=x<3 and 0<=y<3:
        big_cell_i = 0
        big_cell_j = 0
    elif 3<=x<6 and 0<=y<3:
        big_cell_i = 0
        big_cell_j = 1
    elif 6<=x<9 and 0<=x<3:
        big_cell_i = 0
        big_cell_j = 2
    elif 0 <= x < 3 and 3 <= y < 6:
        big_cell_i = 1
        big_cell_j = 0
    elif 3 <= x < 6 and 3 <= y < 6:
        big_cell_i = 1
        big_cell_j = 1
    elif 6 <= x < 9 and 3 <= x < 6:
        big_cell_i = 1
        big_cell_j = 2
    elif 0 <= x < 3 and 6 <= y < 9:
        big_cell_i = 2
        big_cell_j = 0
    elif 3 <= x < 6 and 6 <= y < 9:
        big_cell_i = 2
        big_cell_j = 1
    elif 6 <= x < 9 and 6 <= x < 9:
        big_cell_i = 2
        big_cell_j = 2

    c = big_cell_i * 3
    v = big_cell_j * 3

    for dx in range(3):
        for dy in range(3):
            arr.append(board[c+dx][v+dy])
            board[c + dx][v + dy] = "*"

        ze = 0
        de = board[x][y]
        for i in arr:
            if i == de:
                ze = ze + 1
        if ze > 1:
            return False
        else:
            return True


"""
# draw first board
for row in board:
    for number in row:
        if number == 0:
            point += 1
            print("." ,end=" ")
        else:
            print(number ,end=" ")

    print()

print(point)
"""

def check1():
    return check0(x,y)
    #if board[0][0] != board [0][i] and board[0][0] != board[i][0] and check0(0,i)=True:


for i in range(9):
    for row in board:
        for number in row:
            if board[i][number] != board[row][number] and board[row][number] != board[number][row] and check0(row,number)==True:
                point = point + 1




"""
arr = []
for i in range(9):
    if board[0][0] != board [0][i] and board[0][0] != board[i][0] and check0(0,i)=True:
        arr.append()
"""

c = big_cell_i * 3
v = big_cell_j * 3

for dx in range(3):
    for dy in range(3):
        arr.append(board[c + dx][v + dy])
        board[c + dx][v + dy] = "*"



#print(board[0:])
print(point)


print(check0(1,7))


#print(check1(1,7))