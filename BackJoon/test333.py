import math

width = 51
height = 37
diagonals = [[17,19]]

def calculate(width,height):
    a=math.factorial(width+height)
    b=math.factorial(width)*math.factorial(height)
    
    return int(a/b)
    
    
print(diagonals[0])
res = 0
for i in range(len(diagonals)):
    a=diagonals[i]

    x=a[0]
    y=a[1]
    n=calculate(x-1,y)
    m=calculate(x,y-1)
    n1=(n*calculate(width-x,height-y+1))
    m1=(m*calculate(width-x+1,height-y))
    res+=(n1+m1)
answer=(res)%10000019
print(answer)

    

