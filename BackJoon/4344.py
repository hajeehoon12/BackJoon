import sys
c = int(sys.stdin.readline())

for i in range(c):
    nums = list(map(int, sys.stdin.readline().split()))

    avg = sum(nums[1:])/nums[0]

    cnt = 0

    for score in nums[1:]:
        if score > avg:
            cnt += 1
    rate = (cnt/nums[0])* 100
    print(f'{rate:.3f}%')