import sys
from collections import Counter

n= int(sys.stdin.readline())
num = []
for _ in range(n):
    num.append(int(sys.stdin.readline()))
num.sort()
a = round(sum(num)/n)
b = num[(n-1)//2]

c = 0
if n ==1:
    c = num[0]
else:
    cnt = Counter(num).most_common(2)
    if cnt[0][1] == cnt[1][1]:
        c = cnt[1][0]
    else:
        c = cnt[0][0]

d = max(num)-min(num)

print(a)
print(b)
print(c)
print(d)