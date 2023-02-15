import sys
a = int(sys.stdin.readline())

b = sys.stdin.readline()
result =0 
for i in range(a):
    result += int(b[i])
print(result)