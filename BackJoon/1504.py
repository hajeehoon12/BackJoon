import sys
import heapq
from collections import deque
INF = int(10 ** 9)

n , e = map(int, input().split())


graph = [[] for _ in range(n+1)]


for i in range(e):
    a,b,c = map(int, sys.stdin.readline().rstrip().split())
    
    graph[a].append([b,c])
    graph[b].append([a,c])


def dijkstra(start):
    distance = [INF for _ in range(n+1)]
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    return distance

v1, v2 = map(int, input().split())

original_distance = dijkstra(1)
v1_distance = dijkstra(v1)
v2_distance = dijkstra(v2)

v1_path = original_distance[v1] + v1_distance[v2] + v2_distance[n]
v2_path = original_distance[v2] + v2_distance[v1] + v1_distance[n]

result = min(v1_path, v2_path)
print(result if result < INF else -1)