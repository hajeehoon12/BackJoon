import sys

n = int(input())

def detect(x):
    if x ==1 or x==0: # 0이나 1도 생각해줘야됨
        return 0
    for i in range(2, int(x**0.5)+1):
        if x%i ==0:
            return 0
    return 1


for i in range(n):
    k = int(input())

    while 1:
        if detect(k):
            print(k)
            break
        else:
            k = k+1
