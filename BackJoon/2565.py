import sys

input = sys.stdin.readline

n = int(input())
wire = []
for i in range(n):
    temp = list(map(int, input().rstrip().split()))
    wire.append(temp)

wire.sort(key = lambda x:x[0])

wire_sec = []
for i in range(n):
    wire_sec.append(wire[i][1])

dp = [1] * (n+1)

for i in range(n):
    for j in range(i):
        if wire_sec[i] > wire_sec[j]:
            dp[i] = max(dp[i],dp[j]+1)

print(n-max(dp))