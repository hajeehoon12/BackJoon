import sys

n= int(sys.stdin.readline())

result = 0 

for i in range(1,n+1):
    a = list(map(int,str(i)))       # 자릿수로 나누기
    result = i + sum(a)
    if result == n:
        print(i)
        break

    if i==n:
        print(0)