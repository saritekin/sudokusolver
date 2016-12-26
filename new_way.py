row= [0] * 9
board = []
point = 0
ao = [1,2,3,4,5,6,7,8,9]

for i in range(9):
     board.append(row[:])

# the game
"""board[0][1] = 2
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
"""
def pBoard(x,y,c):
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
    board[x][y] = c
    


pBoard(0,0,6)


def diff(a, b):
    xa = [i for i in set(a) if i not in b]
    xb = [i for i in set(b) if i not in a]
    return xa + xb


#check small cells
def check0(x,y):
    arr = []
    cor = board[x][y]
    # seperate big cells
    big_cell_i = x//3
    big_cell_j = y//3

    c = big_cell_i * 3
    v = big_cell_j * 3

    for dx in range(3):
        for dy in range(3):
            if board[c+dx][v+dy] != 0:
                arr.append(board[c+dx][v+dy])
            #board[c + dx][v + dy] = "*"
    return diff(arr,ao)


#check x
def arr_h(x,y):
    #global board
    arr_h = []
    for i in range (9):
        if board[x][y] == 0 and board[x][y] != board[x][i]:
                arr_h.append(board[x][i])
    return diff(arr_h,ao)


#check y
def arr_v(x,y):
    #global board
    arr_v = []
    for i in range(9):
        if board[x][y] == 0 and board[x][y] != board[i][y]:
                arr_v.append(board[i][y])
    return diff(arr_v,ao)


def snc(ar1,ar2):
    ar3 = []
    for i in ar1:
        for e in ar2:
            if i == e:
                ar3.append(i)
    return ar3[0:]

def main_snc(x,y):
    if board[x][y] == 0:
        a1 = snc(arr_h(x, y), arr_v(x, y))
        a2 = check0(x,y)
        c = snc(a1, a2)
        #return (x,y),c
        return c
    else :
        return  "a"

#print(main_snc(0, 6))

"""def control():
    b  = 0
    for i in range(9):
        for e in range(9):
            if board[i][e] == 0:
                b += 1
            if b == 0 :
                return break
"""


for i in range(9):
    for e in range(9):
        if len(main_snc(i,e)) == 1 and main_snc(i,e) != "a" :
            for d in main_snc(i,e):
                pBoard(i,e,d)
                b = 0



# draw first board
for row in board:
    for number in row:
        if number == 0:
            point += 1
            print(".", end=" ")
        else:
            print(number, end=" ")

    print()


#print(la(0,6))
#def check_fnl():


