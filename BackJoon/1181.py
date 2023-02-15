import sys
N = int(sys.stdin.readline())
a= []
for i in range(N):
    a.append(sys.stdin.readline().strip())
a = list(set(a))
a.sort()
a.sort(key=len)
for i in a:
    print(i)


