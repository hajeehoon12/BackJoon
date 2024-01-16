import sys
from collections import deque

n= int(input())

graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
q = deque()
q.append(1)

for i in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)



while q:
    x = q.popleft()

    for i in graph[x]:
        if visited[i] == 0:
            visited[i] = x
            q.append(i)

for i in range(2, n+1):
    print(visited[i])