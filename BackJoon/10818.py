import sys
a = int(sys.stdin.readline())
b = list(map(int , sys.stdin.readline().split()))
print(min(b), max(b))