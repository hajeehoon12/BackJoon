import sys

a= list(map(int,sys.stdin.readline().strip().split()))
b = []

for i in range(len(a)-1):
    if a[i] == 0:
        b.append(i)
        
c = len(b)
d = 0
for i in b:
    k = i -d
    del a[k]
    d +=1
for i in range(d):
    a.extend([0])

print(a)