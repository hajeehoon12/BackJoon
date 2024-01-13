import sys
input = sys.stdin.readline
import heapq
from collections import defaultdict

INF = int(1e9)

n = int(input())
m = int(input())

graph = defaultdict(list)


for _ in range(m):
    a, b, c = map(int, input().rstrip().split())
    graph[a].append((b,c))

start, end = map(int, input().rstrip().split())

dist = [INF] * (n+1)
prev_node = [0] * (n+1)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0 , start))
    dist[start] = 0
    while q:
        weight, node =heapq.heappop(q)

        if dist[node] < weight:
            continue
        
        for adj_node, adj_cost in graph[node]:
            cost = weight + adj_cost
            if cost < dist[adj_node]:
                prev_node[adj_node] = node
                dist[adj_node] = cost
                heapq.heappush(q, (cost, adj_node))

dijkstra(start)
print(dist[end])

path = [end]
cur_path = end

while cur_path != start:
    cur_path = prev_node[cur_path]
    path.append(cur_path)

print(len(path))
print(' '.join(map(str, reversed(path))))
