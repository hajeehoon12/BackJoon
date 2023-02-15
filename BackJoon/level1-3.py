n = 45

d = [0] * (n+1)

def stair(x):
    if x==1:
        return 1
    if x==2:
        return 2
    if d[x] !=0:
        return d[x]
    d[x] = stair(x-1) + stair(x-2)
    return d[x]

print(stair(45))
        





