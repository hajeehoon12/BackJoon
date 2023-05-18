import sys
input = sys.stdin.readline

n = int(input())

paper = [list(map(int, input().rstrip().split())) for _ in range(n)]

result_w = 0
result_b = 0

def solution(x,y, n):
    global result_w,result_b
    color = paper[x][y] # basic value of fraction of paper
    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != paper[i][j]: # if not match with basic value

                solution(x, y, n//2)
                solution(x, y+n//2, n//2)
                solution(x+n//2, y, n//2)
                solution(x+n//2, y+n//2, n//2)
                return
    if color ==0:
        result_w +=1
    else:
        result_b +=1

solution(0,0,n)

print(result_w)
print(result_b)

