import sys


a,b,c = map(int, sys.stdin.readline().split())

if b>= c : 
    print(-1)
else:
    num=int(a/(c-b) +1)
    print(num)