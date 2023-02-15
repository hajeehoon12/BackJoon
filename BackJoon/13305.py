import sys

number = int(sys.stdin.readline())          #길이
length = list(map(int,sys.stdin.readline().strip().split()))  #도시간길이
city = list(map(int,sys.stdin.readline().strip().split()))    #주유소가격

cost = city[0] * length[0] #결괏값 초기화

compare = city[0] # 비교하기 위한 값
distance = 0    # 거리 초기화


for i in range(1, number-1):
    if city[i] < compare:
        cost += compare*distance
        distance = length[i]
        compare = city[i]
    else:
        distance += length[i]

    if i == number-2:
        cost += compare*distance

print(cost)

