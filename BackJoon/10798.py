import sys

c= [[0]* 15 for i in range(5)]

for i in range(5):
    d = list(sys.stdin.readline().rstrip())
    
    for j in range(len(d)):
        c[i][j] = d[j]

for i in range(15):
    for j in range(5):
        if c[j][i] == 0:
            continue;
        else:
            print(c[j][i], end ='')


