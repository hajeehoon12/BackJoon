import sys
input = sys.stdin.readline

str = input()
list = []
for i in str:
    list.append(i)
list_1=list.sort(reverse =True)

for i in list_1:
    print(i , end = '')