import sys

n = int(input())

num_list = list(map(int, sys.stdin.readline().split()))

result = [-1] * n

temp = [0]

for i in range(1,n):
    #print(temp)
    while temp and num_list[temp[-1]] < num_list[i]: # 찾는과정
        result[temp.pop()] = num_list[i] # 찾으면 대체 못찾으면 -1이 default
        
    temp.append(i) # 다음단계
#print(temp)
print(*result)