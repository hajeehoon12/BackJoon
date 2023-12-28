N, K = int(input()), int(input())
start, end = 1, K

def binary_search(target, start, end):
    while start <= end:
        mid = (start + end) // 2

        cnt = 0
        for i in range(1, N+1):
            cnt += min(mid//i, N)

        if cnt >= target: # 초과하면 아래서 찾음
            end = mid-1
        else: # 낮으면 위에서 찾음
            start = mid+1
    return start
print(binary_search(K, 1, N*N))