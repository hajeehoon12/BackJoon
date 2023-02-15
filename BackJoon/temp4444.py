
targets = [2,1,1,5,6,4]

answer = []
m=len(targets)
a= {}
c ={}
for i in range(m):
    a[i] = 1        #받은거
for i in range(m):
    c[i] = 0        #먹은거


d = {}

for i in range(10):
    for i in range(m):
        d[i] = 0
    for i in range(m):
        if a[i] >= 2:
            b=a[i]-1
            a[i] = 1
            c[i] += b
    for i in range(m):
        if a[i] ==1:
            a[i] = 0
            t=targets[i]-1
            d[t] += 1
    for i in range(m):
        a[i] += d[i]
answer = list(c.values())
print(answer)