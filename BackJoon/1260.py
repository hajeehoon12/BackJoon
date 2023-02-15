from collections import deque
import sys

def bfs(v): # 너비 우선탐색
    q = deque()
    q.append(v)
    visit_list[v] = 1
    while q:
        v= q.popleft()
        
        print(v, end = " ")
        for i in range(1, n+1):
            if visit_list[i] == 0 and graph[v][i] == 1 :
                q.append(i)
                visit_list[i] = 1



def dfs(v): # 깊이 우선탐색
    visit_list2[v] =1  # 거기에방문했다 초기화
    print(v, end = " ")
    for i in range(1, n+1):
        if visit_list2[i] == 0  and graph[v][i] == 1: # 기존에 안들렸었고, 다음꺼와 연결되있다면
            dfs(i)


n,m,v = map(int, sys.stdin.readline().split())

graph = [[0] * (n+1) for _ in range(n+1)]
visit_list = [0] * (n+1)   # bfs방문
visit_list2 = [0] * (n+1)   # dfs 방문

for _ in range(m):
    a,b = map(int, sys.stdin.readline().split())
    graph[a][b] = graph[b][a] = 1  # 연결되있다를 표시

dfs(v)
print()
bfs(v)
