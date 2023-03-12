import sys

a1,b1 = map(int, sys.stdin.readline().split())
a2,b2 = map(int, sys.stdin.readline().split())

c1,c2=a1*b2+b1*a2,b1*b2
d1,d2=c1,c2
while c1%c2 !=0:
        c1,c2=c2,c1%c2

print(int(d1/c2),int(d2/c2))
