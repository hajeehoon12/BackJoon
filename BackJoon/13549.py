from collections import deque

n , k = map(int, input().split())



#print(len(graph))

def bfs(start):
    distance = [-1 for _ in range(100001)]

    q = deque()
    q.append(start)
    distance[start] = 0

    while q:
        x= q.popleft()
        if x ==k:
            return distance[x]
        #print(x)
        
        if 0<2*x < 100001 and distance[x*2] == -1: # 0에서 무한으로 도는거 체크
            distance[x*2] = distance[x]
            q.appendleft(x*2)

        if 100001>x-1 >= 0 and distance[x-1] == -1:
            distance[x-1] = distance[x]+1
            q.append(x-1)

        if 0<=x+1 < 100001 and distance[x+1]== -1:
            distance[x+1] = distance[x]+1
            q.append(x+1) 

print(bfs(n))