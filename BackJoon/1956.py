import heapq as hq
import sys

V, E = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(V+1)]

INF = 1e9

dist = [[1e9]*(V+1) for _ in range(V+1)]

heap = []

for _ in range(E):
    a,b,c = map(int, sys.stdin.readline().split())
    hq.heappush(heap ,[c, a, b])
    graph[a].append([b,c])
    dist[a][b] = c

while heap:
    cost, start, stop = hq.heappop(heap)
    #print(cost, start ,stop)
    if start == stop:
        print(cost)
        break

    if dist[start][stop] < cost:
        continue

    for temp_stop, temp_cost in graph[stop]:
        new_distance = cost + temp_cost
        
        if new_distance < dist[start][temp_stop]:
            dist[start][temp_stop] = new_distance
            hq.heappush(heap, [new_distance, start, temp_stop])

else:
    print(-1)