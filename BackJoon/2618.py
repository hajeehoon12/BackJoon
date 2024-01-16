import sys
sys.setrecursionlimit(10**7)

n= int(input())
w =int(input())

s = []
path = []

dp = [[-1]*(w+1) for _ in range(w+1)]
for _ in range(w):
    p, q = map(int, sys.stdin.readline().rstrip().split())
    s.append((p,q))
s1 = [(1,1)]+s
s2 = [(n,n)]+s

def f(p1, p2, n, w):
    if p1 == w or p2 == w:
        return 0 
    if dp[p1][p2] != -1:
        return dp[p1][p2]
    x= s1[p1][0]    # x,y = p1 a,b = p2
    y= s1[p1][1]
    a= s2[p2][0]
    b= s2[p2][1]

    next = max(p1, p2) + 1

    l1 = abs(s[next-1][0] - x) + abs(s[next - 1][1] - y)
    l2 = abs(s[next-1][0] - a) + abs(s[next - 1][1] - b)
    
    if(l1 + f(next,p2,n,w) <l2+ f(p1,next,n,w)):
        path.append(1)
        dp[p1][p2] = l1 + f(next,p2,n,w)
    else:
        path.append(2)
        dp[p1][p2] = l2 +f(next,p1,n,w)

    return dp[p1][p2]

k = 0

print(f(0,0,n,w))
for i in reversed(path):
    k +=1
    
    print(i)
    if k==w:
        break