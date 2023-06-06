import sys
input = sys.stdin.readline
a,b = map(int, input().rstrip().split())
list_a = set(map(int, input().rstrip().split()))
list_b = set(map(int, input().rstrip().split()))

print(a+b - 2*(len(list_a & list_b)))