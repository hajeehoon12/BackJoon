
point = 2
n = int(input())

for i in range(n):
    point += point-1

print(point **2)