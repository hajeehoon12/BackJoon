import sys
a = int(sys.stdin.readline())
 
zero = [1,0]
one = [0,1]
 
def cal(num):
    length = len(zero)
    if length <= num:
        for i in range(length,num+1):
            zero.append(zero[i-1]+zero[i-2])
            one.append(one[i-1]+one[i-2])
    print(zero[num], one[num])
 
for i in range(a):
    k = int(sys.stdin.readline())
    cal(k)

