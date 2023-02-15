import sys
A = int(sys.stdin.readline())

for i in range(1,A+1):
    for _ in range(A-i):
        print(" ", end='')
    for _ in range(i):
        print("*", end='')
    print("")