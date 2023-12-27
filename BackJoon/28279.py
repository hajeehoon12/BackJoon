import sys
from collections import deque
n = int(input())

queue = deque()
for i in range(n):

    num = list(map(int, sys.stdin.readline().split()))

    if num[0] == 1:
        queue.appendleft(num[1])
    elif num[0] == 2:
        queue.append(num[1])
    elif num[0] == 3:
        print(queue.popleft() if queue else -1)
    elif num[0] == 4:
        print(queue.pop() if queue else -1)
    elif num[0] == 5:
        print(len(queue))
    elif num[0] == 6:
        print(0 if queue else 1)
    elif num[0] == 7:
        print(queue[0] if queue else -1)
    elif num[0] == 8:
        print(queue[-1] if queue else -1)