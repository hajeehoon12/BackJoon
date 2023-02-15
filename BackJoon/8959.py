import sys
a = int(sys.stdin.readline())

for _ in range(a):
    b = sys.stdin.readline()
    result = 0
    cnt = 0
    for i in b:
        if i == "O":
            cnt += 1
        else:
            cnt = 0
        result +=cnt
    print(result)