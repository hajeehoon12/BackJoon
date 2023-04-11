import sys
input = sys.stdin.readline

n= int(input())

for i in range(n):
    temp = input()
    temp2 = True
    count = 0
    for j in temp:
        if count <0:
            print("NO")
            temp2 = False
            break
        elif j == "(":
            count +=1
        if j == ")":
            count -=1
    if count ==0:
        print("YES")
    else:
        if temp2 ==True:
            print("NO")
