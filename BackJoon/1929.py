import sys

a, b = map(int, sys.stdin.readline().split())

def detect(x):
    if x == 1:
        return 0
    for i in range(2,int(x**0.5)+1): # 
        if x%i == 0:
            return 0 
    return 1 

for i in range(a,b+1):
    if detect(i):
        print(i)