
row= [0] * 9
board = []

for i in range(9):
     board.append(row[:])

# problem
board[0][3] = 2
board[2][7] = 5
board[1][4] = 8

# cells
big_cell_i = 0
big_cell_j = 1

x = big_cell_i * 3
y = big_cell_j * 3

# seperate big cells

for dx in range(3):
    for dy in range(3):
        board[x+dx][y+dy] = "*"

# ...
for row in board:
    for number in row:
        if number == 0:
            print(".", end=" ")
        else:
            print(number, end=" ")
    print()



board[0][6] = 7
board[3][2] = 3
board[4][7] = 5
board[0][8] = 4
board[3][8] = 7
board[0][2] = 8
board[8][8] = 9
board[0][4] = 1
board[4][6] = 2
board[1][1] = 9
board[4][4] = 6
board[5][2] = 2
board[5][8] = 3
board[0][7] = 9
board[2][1] = 1
board[3][5] = 9
board[0][0] = 3
board[2][7] = 8
board[3][0] = 6
board[4][3] = 1
board[5][1] = 8
board[2][3] = 9
board[2][5] = 4
board[4][0] = 9
board[2][4] = 2
board[5][0] = 1
board[5][5] = 7
board[1][5] = 8
board[2][8] = 5
board[5][3] = 5
board[1][3] = 7
board[1][8] = 2
board[5][4] = 4
board[6][6] = 5
board[6][7] = 7
board[6][8] = 6
board[7][4] = 5
board[7][5] = 6
board[8][0] = 5
board[8][1] = 6
board[6][1] = 3
board[6][2] = 4
board[7][0] = 8
board[6][0] = 2
board[6][3] = 8
board[7][3] = 3

"""if 0<=x<3 and 0<=y<3:
     big_cell_i = 0
     big_cell_j = 0
 elif 3<=x<6 and 0<=y<3:
     big_cell_i = 0
     big_cell_j = 1
 elif 6<=x<9 and 0<=y<3:
     big_cell_i = 0
     big_cell_j = 2
 elif 0 <= x < 3 and 3 <= y < 6:
     big_cell_i = 1
     big_cell_j = 0
 elif 3 <= x < 6 and 3 <= y < 6:
     big_cell_i = 1
     big_cell_j = 1
 elif 6 <= x < 9 and 3 <= y < 6:
     big_cell_i = 1
     big_cell_j = 2
 elif 0 <= x < 3 and 6 <= y < 9:
     big_cell_i = 2
     big_cell_j = 0
 elif 3 <= x < 6 and 6 <= y < 9:
     big_cell_i = 2
     big_cell_j = 1
 elif 6 <= x < 9 and 6 <= y < 9:
     big_cell_i = 2
     big_cell_j = 2"""



