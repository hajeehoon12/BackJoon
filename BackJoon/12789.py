b= []

n= int(input())

a=list(map(int, input().split()))

post = 1
result = 1
while a or b:
    
    if not a and b[0] != post:
        result = 0
        break 


    if a:
        if a[0] == post:
            post +=1
            a.pop(0)
            continue
    if b:
        if b[0] ==post:
            post +=1
            b.pop(0)
            continue
    
    b.insert(0, a.pop(0))
    

if result:
    print("Nice")
else:
    print("Sad")
