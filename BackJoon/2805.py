import sys

n, m = map(int,sys.stdin.readline().split())

length = list(map(int,sys.stdin.readline().split()))

start, end = 1, max(length)

def binary(m,start,end):
    if start > end:
        return end
    mid = (start+end)//2
    amount = 0
    for i in length:

        if mid <= i:
            amount+=i-mid
        else:
            continue
    
    if amount >= m:
        return binary(m,mid+1,end)
    else:
        return binary(m,start,mid-1)

print(binary(m,start,end))