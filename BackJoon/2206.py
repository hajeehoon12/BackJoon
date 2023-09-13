from collections import deque
import sys

n, m = map(int, input().split())

graph = [list(map(int,sys.stdin.readline().rstrip())) for _ in range(n)]

visited = [[[0] *2 for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1

#print(graph)

dx = [1,0,0,-1]
dy = [0,1,-1,0]
q = deque([[0,0,0]])

def bfs():
    while q:
        x,y,z = q.popleft()
        #print(x,y,z)
        if x==n-1 and y ==m-1:
            print(visited[x][y][z])
            return 
        for i in range(4):
            cx,cy = x+dx[i],y+dy[i]

            if 0<= cx< n and 0<= cy < m:
                if graph[cx][cy] == 1 and z ==0:
                    visited[cx][cy][1] = visited[x][y][z] + 1
                    q.append((cx,cy,1))
                if graph[cx][cy] == 0 and visited[cx][cy][z] == 0 :
                    visited[cx][cy][z] = visited[x][y][z] + 1
                    q.append((cx,cy,z))
    print(-1)
    return  # 끝날때까지 해결안된 경우


bfs()


