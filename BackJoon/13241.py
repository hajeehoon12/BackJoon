import sys

a,b = map(int, sys.stdin.readline().strip().split())
a1,b1 = a,b

while a%b !=0:
    a,b=b,a%b

print(a1*b1//b)
