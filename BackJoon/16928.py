from collections import deque

n, m = map(int, input().split())

lad = dict()
snake = dict()

for _ in range(n):
    x,y = map(int,input().split())
    lad[x] = y
for _ in range(m):
    x,y = map(int,input().split())
    snake[x] = y

graph = [0]* 101

dx = [1,2,3,4,5,6]

q = deque()


def bfs(start):
    
    q.append(start)
    graph[start] = 1

    while q:
        #print(q)
        x = q.popleft()
        for i in range(6):
            nx=dx[i]+x
            if nx < 100 and graph[nx] == 0:

                if nx in lad.keys():
                    nx = lad[nx]
                elif nx in snake.keys():
                    nx = snake[nx]
                if graph[nx] == 0:
                    graph[nx] = graph[x] + 1
                    q.append(nx)
            elif nx == 100:
                return graph[x]
            
print(bfs(1))