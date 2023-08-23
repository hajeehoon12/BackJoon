import sys
import heapq

input = sys.stdin.readline

n= int(input())
pq = []
for _ in range(n):
    x = int(input())

    if x != 0:
        heapq.heappush(pq, (abs(x), x))
    else:
        if len(pq) >= 1:
            print(heapq.heappop(pq)[1])
        else:
            print(0)