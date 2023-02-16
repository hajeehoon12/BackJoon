import sys
n= int(sys.stdin.readline())
cnt = 0
temp = n
while True:
    a=n//10
    b=n%10
    c=(a+b)%10
    n = 10 * b + c
    cnt += 1

    if(n == temp):
        break
print(cnt)