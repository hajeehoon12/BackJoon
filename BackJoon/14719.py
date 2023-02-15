import sys

height, width = map(int, sys.stdin.readline().split())
size = list(map(int, sys.stdin.readline().split()))

area = 0
for i in range(1, width - 1):
    # 지금 위치의 왼쪽 블록 중 자신보다 큰 가장 큰 높이를 찾는다.
    left_height = size[i]
    for j in range(i - 1, -1, -1):
        if left_height < size[j]:
            left_height = size[j]
        # 현재 위치의 오른쪽 블록 중 자신보다 큰 가장 큰 높이를 찾는다.
    right_height = size[i]
    for j in range(i + 1, width):
        if right_height < size[j]:
            right_height = size[j]
        # 왼쪽, 오른쪽 높이 중 작은 높이에서 현재 높이를 뺀 값을 더한다.
    
    area += min(left_height, right_height) - size[i]

print(area)