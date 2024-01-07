import sys

n= int(input())
xx = []
yy = []
for i in range(n):
    a, b = map(int , sys.stdin.readline().rstrip().split())
    xx.append(a)
    yy.append(b)

xxx = max(xx) - min(xx)
yyy = max(yy) - min(yy)
print(xxx * yyy)