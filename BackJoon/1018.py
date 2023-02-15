import sys
A,B = map(int,sys.stdin.readline().split())
board = []
for _ in range(A):
    board.append(sys.stdin.readline())
temp= []

for x in range(A-7):
    for y in range(B-7):
        result1 = 0  # 두가지케이스로 나눔 result 1은 W로시작할때
        result2 = 0  # result2는 B로 시작할때
        for a in range (x, x+8):
            for b in range(y, y+8):
                if (a+b)%2 == 0:
                    if board[a][b] != 'W': result1 +=1 # 첫번째칸기준생각 기준
                    if board[a][b] != 'B': result2 +=1
                else:
                    if board[a][b] == 'W': result1 +=1 # 첫번째옆 대각선칸기준
                    if board[a][b] == 'B': result2 +=1
        
        temp.append(result1)
        temp.append(result2)
print(min(temp)) # 넣은경우의수값중 최솟값