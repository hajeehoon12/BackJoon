

n= int(input())
m = int(input())
pair = [[] for _ in range(n+1)]
visited = [0] * (n+1)
#print(visited)
result = 0
for _ in range(m):
    a,b = map(int, input().split())
    pair[a].append(b)
    pair[b].append(a)
#print(pair)

def dfs(x):
    visited[x] =1
    for j in pair[x]:
        if visited[j] == 0:
            dfs(j)

dfs(1)
print(sum(visited)-1)

