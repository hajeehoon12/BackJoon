import sys
n = int(sys.stdin.readline())
numbers = map(int, sys.stdin.readline().split())
decimal = 0
for num in numbers:
    error = 0
    if num > 1:
        for i in range(2,num):
            if num%i ==0:
                error+=1
        if error == 0:
            decimal +=1
print(decimal)