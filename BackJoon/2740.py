import sys

n, m = map(int, sys.stdin.readline().split())

A = []
for i in range(n):
    A.append(list(map(int, sys.stdin.readline().split())))

m , k = map(int, sys.stdin.readline().split())

B= []

for _ in range(m):
    B.append(list(map(int, sys.stdin.readline().split())))

C = [[0 for _ in range(k)] for _ in range(n)]

for i in range(n):
    for h in range(m):
        for j in range(k):
        
            C[i][j] += A[i][h] * B[h][j]

for i in C:
    for j in i:
        print(j, end = ' ')
    print()

