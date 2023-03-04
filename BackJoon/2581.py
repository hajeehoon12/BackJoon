import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

list = []

for num in range(n, m+1):
    error = 0
    if num > 1:
        for i in range(2, num-1):
            if num % i == 0:
                error +=1
                break
        if error==0:
            list.append(num)

if len(list) > 0 :
    print(sum(list))
    print(min(list))
else:
    print(-1)