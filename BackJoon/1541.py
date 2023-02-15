import sys
 
Sum = 0
num = 0
B = (sys.stdin.readline().strip().split('-'))
first = True


for i in B:
    A=list(map(int,(i.split('+'))))
   
    if first==True:
        Sum = sum(A)
        num +=Sum
        first = False
    else:
        Sum = sum(A)
        num -=Sum

print(num)

