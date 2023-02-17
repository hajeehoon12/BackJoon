import sys

num_list = []
for _ in range(10):
    n = int(sys.stdin.readline())
    num_list.append(n%42)
num_list = set(num_list)

print(len(num_list))