from collections import deque
import sys
n,m,r = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]

visited = [0] * (n+1)

for _ in range(m):
    a,b = map(int, sys.stdin.readline().split())

    graph[a].append(b)
    graph[b].append(a)

for i in range(n+1):
    graph[i].sort(reverse=True)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = 1
    cnt = 1

    while queue:
        v = queue.popleft()

        for i in graph[v]:
            if not visited[i]:
                cnt += 1
                visited[i] = cnt
                queue.append(i)
                



bfs(graph, r, visited)
#print(visited)
for i in range(1, n+1):
    print(visited[i])