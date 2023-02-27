import sys


n1= int(sys.stdin.readline())
n2= int(sys.stdin.readline())
c=n2//100
b=(n2%100)//10
a=n2%10
print(n1*a)
print(n1*b)
print(n1*c)
print(n1*n2)
