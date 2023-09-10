import sys
from collections import deque

n = int(input())

apa = [list(map(int, input())) for _ in range(n)]

#print(mapp)

dx = [0,0,1,-1]
dy = [1,-1,0,0]
#print(len(mapp))
def bfs(apa, x, y):
    n = len(apa)
    queue = deque()
    queue.append((x,y))
    apa[x][y] = 0
    count = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx <0 or nx >= n or ny< 0 or ny>=n:
                continue
            if apa[nx][ny] == 1:
                apa[nx][ny] = 0
                queue.append((nx,ny))
                count+=1
    return count

result = []
for i in range(n):
    for j in range(n):
        #print(apa[i][j])
        if apa[i][j] == 1:
            result.append(bfs(apa,i,j))

result.sort()
print(len(result))
for i in result:
    print(i)