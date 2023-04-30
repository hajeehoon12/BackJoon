import sys
n= int(sys.stdin.readline())
k = []
for i in range(n):
    k.append(int(sys.stdin.readline()))

dp = [0] *101

dp[1] = 1
dp[2] = 1
dp[3] = 1
dp[4] = 2
dp[5] = 2


for i in range(6, 101):
    dp[i] = dp[i-5] + dp[i-1]

for i in k:
    print(dp[i])
