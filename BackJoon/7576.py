import sys
from collections import deque 



m, n = map(int, input().split())

graph = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]

#print(graph)
q = deque()

for i in range(n):
    for j in range(m):
        if graph[i][j] ==1:
            q.append([i,j])
#print(q)
def bfs():
    dx = [1,0,0,-1]
    dy = [0,1,-1,0]
    
    while q:
        x,y = q.popleft() # i,j = n,m
        #print(x,y)
        for i in range(4):
            cx = dx[i] + x
            cy = dy[i] + y
            #print(cx,cy)
            if 0<= cx<n and 0<=cy<m and graph[cx][cy] == 0:
                q.append([cx,cy])
                graph[cx][cy] = graph[x][y] + 1
                #print(graph[cx][cy])
bfs()
ans = 0
#print(graph)
for i in graph:
    #print(i)
    for j in i:
        if j == 0:
            print(-1)
            exit(0) # 안되는걸 찾을시 -1을 출력한 후 시스템 종료
    ans = max(ans, max(i)) # max(graph)시 list형식이기에 해당형식으로 출력
print(ans - 1) # 시작할때 1로 시작했으므로 일수를 구하기 위해 마지막에 -1연산
                
