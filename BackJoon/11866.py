import sys

n, k=map(int,sys.stdin.readline().split())
q= []
i = 0

for i in range(1,n+1):
    q.append(i)


print("<",end ='')

while len(q) > 1:
    i = i+k
    if i > len(q):
        i = i % len(q)
        if i == 0 :
            i = i+ len(q)
    i = i-1
    print(str(q.pop(i)), end=", ")



print("{}>".format(str(q.pop())))