import sys
n = int(sys.stdin.readline())
k = []
for i in range(n):
    k.append(list(map(int, sys.stdin.readline().split())))
k.sort(key=lambda x:(x[0],x[1]))
for i in k:
    print(i[0], i[1])
