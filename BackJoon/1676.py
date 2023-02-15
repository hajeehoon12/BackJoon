import sys
a= int(sys.stdin.readline())

count = 0
while a>=5:
    count += a//5
    a //=5

print(count)


