from itertools import permutations
import sys
n = int(input())
o = ['+','-','*','/']
num = list(map(int,sys.stdin.readline().split()))
op = list(map(int,sys.stdin.readline().split())) # + - * /
oper = []

for i in range(4):
    for j in range(op[i]):
        oper.append(o[i])
 
oper = list(set(permutations(oper,len(oper)))) #순열 이후 중복되는 것들제거
answer = []
for i in oper:
    n = num[0]
    for j in range(len(num)-1):
        if i[j]=='+':
            n += num[j+1]
        elif i[j]=='-':
            n -= num[j+1]
        elif i[j]=='*':
            n *= num[j+1]
        else:
            if n//num[j+1] <0:
                n = -(-n//num[j+1])
            else:
                n = n//num[j+1]
 
    answer.append(n)
print(max(answer))
print(min(answer))

#print(oper)
#print(op)