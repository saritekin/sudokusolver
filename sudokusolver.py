# I haven't got a good algorithm,
# it work just simple sudoku problems it can check horizontally, vertically and small cells


row = [0] * 9
board = []
point = 0
ao = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(9):
    board.append(row[:])

# the game
board[0][1] = 9
board[0][3] = 2
board[0][5] = 4
board[0][6] = 5
board[1][1] = 2
board[1][4] = 5
board[1][5] = 7
board[1][6] = 6
board[1][7] = 3
board[1][8] = 1
board[2][0] = 6
board[2][1] = 7
board[2][4] = 1
board[3][0] = 7
board[3][1] = 5
board[3][2] = 9
board[4][0] = 3
board[4][3] = 8
board[4][5] = 6
board[4][8] = 7
board[5][6] = 3
board[5][7] = 1
board[5][8] = 4
board[6][4] = 9
board[6][7] = 8
board[6][8] = 3
board[7][0] = 8
board[7][1] = 6
board[7][2] = 2
board[7][3] = 1
board[7][4] = 4
board[7][7] = 9
board[8][2] = 4
board[8][3] = 7
board[8][5] = 5
board[8][7] = 2



# diff func1
def diff(a, b):
    xa = [i for i in set(a) if i not in b]
    xb = [i for i in set(b) if i not in a]
    return xa + xb



# check small cells
def check0(x, y):
    arr = []
    cor = board[x][y]
    # seperate big cells
    big_cell_i = x // 3
    big_cell_j = y // 3

    c = big_cell_i * 3
    v = big_cell_j * 3

    for dx in range(3):
        for dy in range(3):
            if board[c + dx][v + dy] != 0:
                arr.append(board[c + dx][v + dy])
                # board[c + dx][v + dy] = "*"
    return diff(arr, ao)


# check horizontally
def arr_h(x, y):
    # global board
    arr_h = []
    for i in range(9):
        if board[x][y] == 0 and board[x][y] != board[x][i]:
            arr_h.append(board[x][i])
    return diff(arr_h, ao)


# check vertically
def arr_v(x, y):
    # global board
    arr_v = []
    for i in range(9):
        if board[x][y] == 0 and board[x][y] != board[i][y]:
            arr_v.append(board[i][y])
    return diff(arr_v, ao)


# another check
def snc(ar1, ar2):
    ar3 = []
    for i in ar1:
        for e in ar2:
            if i == e:
                ar3.append(i)
    return ar3[0:]


# and another ...
def main_snc(x,y):
    if board[x][y] == 0:
        a1 = snc(arr_h(x, y), arr_v(x, y))
        a2 = check0(x, y)
        c = snc(a1, a2)
        # return (x,y),c
        return c
    else:
        return "a"


# total
def count_filled():
    total = 0
    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
                total += 1
    return total


# main func
while(count_filled() != 81):
    found = []
    for i in range(9):
        for j in range(9):
             if board[i][j] == 0:
                 result = main_snc(i,j)
                 if len(result) == 1:
                     found.append((i,j,result[0]))
    print(found)
    for (i,j,num) in found:
        board[i][j] = num


for i in range(9):
    for e in range(9):
        if len(main_snc(i, e)) == 1 and main_snc(i, e) != "a":
            for d in main_snc(i, e):
                pBoard(i, e, d)
                b = 0

# draw board
for row in board:
    for number in row:
        if number == 0:
            point += 1
            print(".", end=" ")
        else:
            print(number, end=" ")

    print()


