import sys

num = []

for _ in range(5):
    n = int(sys.stdin.readline())
    num.append(n)
num.sort()

print(int(sum(num)/5))
print(num[2])