import sys
import heapq

input = sys.stdin.readline
n = int(input())
pq = []

for i in range(n):
    x = int(input())
    if x: # 0이 아닐 경우
        heapq.heappush(pq, (-x, x)) # 최소 힙으로 만들기 위한 튜플 형식 채용
    else: # 0일 경우
        if len(pq) >= 1:
            print(heapq.heappop(pq)[1])
        else:
            print(0)
