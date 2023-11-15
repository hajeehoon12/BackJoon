import sys

INF = int(1e9)

V, E = map(int, sys.stdin.readline().split())

graph = [[INF]*(V+1) for _ in range(V+1)]

for _ in range(E):
    a,b,c = map(int, sys.stdin.readline().split())
    graph[a][b] = c


for i in range(1, V+1):
    for j in range(1, V+1):
        for k in range(1, V+1):
            graph[j][k]  = min(graph[j][k], graph[j][i]+graph[i][k])


result = INF
for i in range(1, V+1):
    result = min(result, graph[i][i])

if result == INF:
    print(-1)
else:
    print(result)