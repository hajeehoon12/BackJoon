import sys
from collections import deque

n = int(input())
queue = deque(enumerate(map(int, input().split())))

ans = []

while queue:
    #print(queue)
    index, value = queue.popleft()
    ans.append(index+1)

    if value >0:
        queue.rotate(-(value-1))
    elif value <0:
        queue.rotate(-value)

print(' '.join(map(str, ans)))