import sys
input = sys.stdin.readline

n = int(input())

a = list(map(int, input().rstrip().split()))
sum = [a[0]]
for i in range(1,n):
    sum.append(max(sum[i-1] + a[i], a[i]))
print(max(sum))