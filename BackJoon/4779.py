import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def div(s, idx): # idx 3등분 중 위치
    ls = len(s)
    if ls == 3 and idx != 1: # 마지막 3등분의 기본값 '- -'
        return '- -'
    elif ls >= 3 and idx == 1: # 가운데 부분 판별시 공백으로 대체
        return s.replace('-', ' ')

    arr = []

    for i in range(0, ls, ls // 3): # 3등분화
        arr.append(string[i:i+ls//3])

    k = div(arr[0], 0) + div(arr[1], 1) + div(arr[2], 2)
    return k


while True:
    minus = '-'
    n = input().rstrip()
    if n == '':
        break
    num = (3 ** int(n))
    if num == 1:
        print(minus)
        continue

    string = minus * num
    ans = div(string, 0)
    print(ans)