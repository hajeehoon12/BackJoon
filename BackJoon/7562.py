from collections import deque

n = int(input())

def bfs():
    queue = deque()
    dx = [-2,-2,-1,-1,1,1,2,2]
    dy = [-1,1,-2,2,-2,2,-1,1]
   
    queue.append((x,y))
    
    while queue:
        cx,cy = queue.popleft()
        if cx == x1 and cy == y1:
            print(graph[cx][cy])
            return 
        for i in range(8):
            newx ,newy =  dx[i] + cx, dy[i] + cy
            if 0<= newx < chess and 0<= newy < chess and graph[newx][newy] == 0:
                graph[newx][newy]=graph[cx][cy]+1
                queue.append((newx,newy))
            


for _ in range(n):
    chess = int(input())
    x, y = map(int, input().split())
    x1,y1 = map(int, input().split())
    graph = [[0]*chess for _ in range(chess)]
    bfs()

            
        


