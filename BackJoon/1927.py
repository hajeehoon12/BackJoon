import sys
import heapq
input = sys.stdin.readline
n = int(input())

pq = []

for _ in range(n):
    num = int(input())
    if num == 0:
        try:
            print(heapq.heappop(pq))
        except:
            print(0)
    else:
        heapq.heappush(pq, num)