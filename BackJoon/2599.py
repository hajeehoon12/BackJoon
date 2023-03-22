N, K = map(int, input().split())
li = list(map(int, input().split()))
t = sum(li[:K])
ans = t
for i in range(K, N):
    t += li[i]
    t -= li[i-K]
    ans = max(ans, t)
print(ans)