import sys

input = sys.stdin.readline

n = int(input())
mat = []

for _ in range(n):
    mat.append(list(map(int, input().split())))

dp = [[0 for _ in range(n)] for _ in range(n)]


for i in range(1, n): # i 대각선에서 오른쪽으로 몇번째칸
    for j in range(0, n-i): # 몇번째 행의 대각선

        if i == 1:
            dp[j][j+i] = mat[j][0] * mat[j][1] * mat[j+i][1]
            continue

        dp[j][j+i] = 2 ** 31

        for k in range(i):
            dp[j][j+i] = min(dp[j][j+i], dp[j][j+k] + dp[j+k+1][j+i] + mat[j][0] * mat[j+k+1][0] * mat[j+i][1])

print(dp[0][n-1]) # dp행렬의 오른쪽 위 값 즉 전체 곱의 최솟값