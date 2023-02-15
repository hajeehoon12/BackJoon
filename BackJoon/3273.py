import sys

n = int(sys.stdin.readline())

li = list(map(int, sys.stdin.readline().split()))
li.sort()

x = int(sys.stdin.readline())

cnt = 0

left, right= 0, n-1

while left != right:
    if li[left] + li[right] ==x:
        cnt +=1
        left +=1

    elif li[left] +li[right] >x:
        right -=1

    else:
        left+=1 
print(cnt)