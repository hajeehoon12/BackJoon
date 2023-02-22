import sys

num_board = []

for _ in range(9):
    num_board.append(list(map(int, sys.stdin.readline().split())))

X = 0 
Y = 0

MAX = -1

for i in range(9):
    for j in range(9):
        if num_board[i][j] > MAX:
            MAX = num_board[i][j]
            X,Y = i+1,j+1

print(MAX)
print(X,Y)