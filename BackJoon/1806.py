import sys

N,S = map(int, sys.stdin.readline().split())

seq = list(map(int, sys.stdin.readline().split()))

sum = 0
ans = 100001
right, left = 0, 0

while True:
    if sum >= S:
        ans = min(ans, right-left)
        sum -= seq[left]
        left +=1
    elif right == N:
        break
    else:
        sum += seq[right]
        right +=1

if ans == 100001:
    print(0)
else:
    print(ans)