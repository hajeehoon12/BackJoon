import sys

n, m = map(int, sys.stdin.readline().split())

byte = list(map(int , sys.stdin.readline().split()))
cost = list(map(int , sys.stdin.readline().split()))

dp = [[0 for i in range(sum(cost)+1)] for j in range(n+1)]

result = sum(cost)

for i in range(n):
    temp_byte = byte[i]
    temp_cost = cost[i]
    for j in range(sum(cost)):

        if j < temp_cost:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-temp_cost] + temp_byte)

        if dp[i][j] >= m:
            result = min (result, j)

print(result)
