import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

for i in range(n):
    func = input().rstrip()
    num = int(input())
    temp_list = deque(input().rstrip()[1:-1].split(","))
    if '' in temp_list:
        temp_list.pop()

    temp_reverse = False
    temp_error = False

    for j in func:
        if j == "R":
            temp_reverse = not(temp_reverse)
        if j == "D":
            if len(temp_list) ==0:
                temp_error = True
                break
            else:
                if temp_reverse ==True:
                    temp_list.pop()
                else:
                    temp_list.popleft()
    if temp_error ==True:
        print("error")
    else:
        if temp_reverse == True:
            temp_list.reverse()
            print("["+",".join(temp_list)+"]") 
        else:
            print("["+",".join(temp_list)+"]") 
