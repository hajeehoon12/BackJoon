import sys
stop = int(sys.stdin.readline())

n = 1
cnt = 1

while n <= stop-1:
    cnt += 1
    n += cnt

k=n-stop
a= cnt-k
b = 1+k
if cnt%2 == 0:
    
    print(a,'/',b, sep='')
elif cnt%2 == 1:
    
    print(b,"/",a, sep='')
    