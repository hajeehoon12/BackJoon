import sys
while True:
    try:
        A, B = map(int, sys.stdin.readline().split())
        if (A,B) == (0,0):
            break
        print(A+B)
        
    except:
        break