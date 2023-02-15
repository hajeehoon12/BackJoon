import sys

n=int(sys.stdin.readline())
m = []
Map = [[ 0 for t in range(40)] for t in range(2)]
Map[0][0] = 1 
Map[0][1] = 0
Map[1][0] = 0
Map[1][1] = 1
for i in range(2,1,40):
    Map[i][0] = int(Map[i-1][0]) + int(Map[i-2][0])
    Map[i][1] = int(Map[i-1][1]) + int(Map[i-2][1])
for i in range(n):
    m.append(map(int,sys.stdin.readline().strip()))
for i in range(n):
    print(Map[m[i]][0], Map[m[i]][0])