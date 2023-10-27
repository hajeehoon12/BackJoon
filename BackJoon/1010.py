import sys


def factorial(n):
    num = 1
    for i in range(1, n+1):
        num *= i
    return num


t = int(sys.stdin.readline())

for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    ans = factorial(m) // (factorial(n) * factorial(m - n))
    print(ans)