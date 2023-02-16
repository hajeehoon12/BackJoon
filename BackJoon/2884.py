import sys
h,m = map(int, sys.stdin.readline().split())

if m >= 45:
    m-=45
elif h>0 and m < 45:
    h -= 1
    m += 15
else:
    h+= 23
    m += 15
print(h,m)