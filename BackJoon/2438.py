import sys
A = int(sys.stdin.readline())

for i in range(A):
    for a in range(i+1):
        print('*',end='')
    print("")