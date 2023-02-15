import sys

n, sum = map(int, sys.stdin.readline().split())
m = []
amount = 0
for i in range(n):
    m.append(int(input()))
for i in range(n-1, -1, -1):
    if sum==0:
        break
    if m[i] >sum:
        continue
    amount += sum//m[i]
    sum %= m[i]
print(amount)
