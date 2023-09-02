import sys
from collections import deque
m,n,h = map(int,input().split()) # mn크기, h상자수
graph = []
queue = deque([])
 
graph = [[list(map(int, sys.stdin.readline().split())) for _ in range(n)] for _ in range(h)]
    
dx = [-1,1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]

for a in range(h):
    for b in range(n):
        for c in range(m):
            if graph[a][b][c] == 1:
                queue.append((a,b,c))

while(queue):
    x,y,z = queue.popleft()
    
    for i in range(6):
        a = x+dx[i]
        b = y+dy[i]
        c = z+dz[i]
        if 0<=a<h and 0<=b<n and 0<=c<m and graph[a][b][c]==0:
            queue.append([a,b,c])
            #print(graph[x][y][z])
            graph[a][b][c] = graph[x][y][z]+1
            
result = 0
for i in graph:
    for j in i:
        for k in j:  
            if k==0:
                print(-1)
                exit(0)
            result = max(result,k)
print(result-1)