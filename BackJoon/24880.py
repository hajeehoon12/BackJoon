import sys
sys.setrecursionlimit(1000000)
N,M,R = map(int, sys.stdin.readline().split())
line = [[] for _ in range(N+1)]
#print(line)
visited = [0] * (N+1)
cnt = 1
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    line[a].append(b)
    line[b].append(a)
def dfs(x):
    global cnt
    visited[x] = cnt
    line[x].sort(reverse=True)
    for i in line[x]:
        if visited[i] ==0:
            cnt += 1
            dfs(i)

dfs(R)
for i in range(1, N+1):
    print(visited[i])



