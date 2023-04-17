import sys
input = sys.stdin.readline

n = int(input())
list = []
for i in range(n):
    list.append(int(input()))

so_list=sorted(list)

for i in so_list:
    print(i)