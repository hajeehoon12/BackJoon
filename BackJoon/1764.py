import sys
input = sys.stdin.readline
n, m = map(int, input().rstrip().split())

a = set()
for _ in range(n):
    a.add(input().rstrip())
b = set()
for _ in range(m):
    b.add(input().rstrip())
result = sorted(list(a & b))
print(len(result))
for i in result:
    print(i)