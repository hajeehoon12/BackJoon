import sys
A = []
sum = 0

length = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))
A.sort()

for i in range(length):
    sum += A[i] * (length-i)
print(sum)

