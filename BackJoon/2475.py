import sys
a= list(map(int, sys.stdin.readline().split()))
result =0
for i in a:
    result +=i*i
print(result%10)