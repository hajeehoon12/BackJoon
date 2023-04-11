import sys
input  = sys.stdin.readline

while True :
    a = input().rstrip()
    stack = []

    if a == '.' :
        break
    temp =True
    for i in a :
        if i == '[' or i == '(' :
            stack.append(i)
        elif i == ']' :
            if len(stack) != 0 and stack[-1] == '[' :
                stack.pop() 
            else : 
                temp =False
                break
        elif i == ')' :
            if len(stack) != 0 and stack[-1] == '(' :
                stack.pop()
            else :
                temp =False
                break
    if len(stack) == 0 and temp==True:
        print('yes')
    else :
        print('no')