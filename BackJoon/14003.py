import sys
from bisect import bisect_left, bisect_right

n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))

q= []
temp = []

for x in a:
    if not q or x>q[-1]:
        q.append(x)
        temp.append((len(q)-1,x))
    else:
        q[bisect_left(q,x)] = x
        temp.append((bisect_left(q,x),x))

ans= []
last_idx = len(q) -1
for i in range(len(temp)-1 , -1, -1):
    if temp[i][0] ==last_idx:
        ans.append(temp[i][1])
        last_idx -=1

print(len(ans))
print(*reversed(ans)) # 출력할때 리스트로 안보이고 나오게하는방법

#입력 : 6 , 10 20 10 30 25 50