import sys
input = sys.stdin.readline

n , m = map(int, input().rstrip().split())

a = list(map(int, input().rstrip().split()))

#print(len(a))

for i in range(len(a)):
    if i ==0:
        a[i] =a[i] % m
    else:
        a[i]=(a[i-1]+a[i]) % m

result = 0


temp = [0]*(m+1)

for i in range(len(a)):
    if a[i] ==0:
        result += 1
    temp[a[i]] += 1

for i in temp:
    result += (i*(i-1))//2
#print(a)
#print(temp)
print(result)