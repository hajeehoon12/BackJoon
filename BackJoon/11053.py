import sys
input = sys.stdin.readline

n = int(input())

num = list(map(int,input().rstrip().split()))
dp = [1] * 1001

for i in range(1,n):
    for j in range(i):
        if num[j] < num[i]:
            dp[i] = max(dp[i],dp[j]+1)
print(max(dp))
