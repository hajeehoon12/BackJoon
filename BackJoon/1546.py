import sys
a = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))
max_b=max(b)
new_b = []
for i in b:
    new_b.append(i/max_b*100)
print(sum(new_b)/a)