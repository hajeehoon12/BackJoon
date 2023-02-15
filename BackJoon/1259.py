import sys
while True:
    n = sys.stdin.readline().strip()

    if n == '0':
        break
    if n == n[::-1]: # 처음부터 끝까지 -1칸 간격으로 1번째칸 처음 2번째칸 끝 3번째칸 간격
        print('yes')
    else:
        print('no')
    