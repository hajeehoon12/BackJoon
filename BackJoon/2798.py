import sys
result = 0
length,sum  = list(map(int,sys.stdin.readline().strip().split()))  #길이, #카드의 합
number = list(map(int,sys.stdin.readline().strip().split()))    #카드의 넘버

for i in range(length):
    for j in range(i+1,length):
        for k in range(j+1,length):
            if number[i] + number[j] + number[k] > sum:
                continue
            else:
                result = max(result,(number[i] + number[j] + number[k]))

print(result)