import sys          # 이분탐색

n,m = map(int,sys.stdin.readline().split())

#length = []
#for i in range(n):
    #length.append(int(sys.stdin.readline().strip()))

length = [int(sys.stdin.readline()) for _ in range(n)]

start, end = 1, max(length)

while start <= end:
    mid = (start+end)//2
    lines = 0
    for i in length:
        lines += i //mid
    if lines >= m:          # lines > m 은 최소값 구하는것 명심!! 지금은 최대값
        start= mid +1
    else:
        end = mid -1
print(end)
