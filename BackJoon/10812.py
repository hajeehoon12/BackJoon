import sys
n,m = map(int, sys.stdin.readline().split())

box = [i+1 for i in range(n)]

for _ in range(m):
    i, j , k = map(int, sys.stdin.readline().split())
    box = box[:i-1]+ box[k-1:j]+box[i-1:k-1]+box[j:]
for b in box:
    print(b, end = ' ')