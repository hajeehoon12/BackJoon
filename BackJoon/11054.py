import sys
input = sys.stdin.readline

n = int(input())

num = list(map(int,input().rstrip().split()))
dp_1 = [0] * n
dp_2 = [0] * n
for i in range(1,n):
    for j in range(i):
        if num[j] < num[i]:
            dp_1[i] = max(dp_1[i],dp_1[j]+1)
num.reverse()
for i in range(1,n):
    for j in range(i):
        if num[j] < num[i]:
            dp_2[i] = max(dp_2[i],dp_2[j]+1)
dp_2.reverse()
max_value = 0
for i in range(n):
    max_value = max(dp_1[i] + dp_2[i],max_value)

print(max_value+1)
