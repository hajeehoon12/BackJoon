import sys
n= int(input())
b = 0
A = []
for _ in range(n):
    A.append(int(sys.stdin.readline()))
A=A+[0]
s = [(0,A[0])]
for i in range(1,n+1):
    c=i
    while s and s[-1][1]>A[i]:
        c,h=s.pop()
        b=max(b,(i-c)*h)
    s.append((c,A[i]))
print(b)
