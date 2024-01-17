import sys
from collections import deque

v= int(input())
tree = [[] for _ in range(v+1)]

for i in range(v):
    a = list(map(int, sys.stdin.readline().rstrip().split()))

    node = a[0]

    index = 1
    while a[index] != -1:
        next_node, next_cost = a[index], a[index+1]
        tree[node].append((next_node, next_cost))
        index += 2


def bfs(start):
    q = deque()
    q.append((start , 0))

    visited = [-1] *(v+1)
    visited[start] = 0
    res = [0, 0]

    while q:
        node, dist = q.popleft()

        for nxt_node, nxt_dist in tree[node]:
            if visited[nxt_node] == -1:
                cal_dist = dist + nxt_dist
                q.append((nxt_node, cal_dist))
                visited[nxt_node] = cal_dist

                if res[1] < cal_dist:
                    res[0] = nxt_node
                    res[1] = cal_dist
    return res

point, _ = bfs(1)
print(bfs(point)[1])