import sys

n = int(input())

temp = dict()

for _ in range(n):
    a,b = map(str, sys.stdin.readline().split())

    if b == "enter":
        temp[a] = 0
    else:
        del temp[a]

temp = sorted(temp, reverse = True)

for i in temp:
    print(i)