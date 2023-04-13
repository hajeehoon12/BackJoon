def Q_range(x): # Queen의 공격범위 검사
    for next in range(x): 
        if row[x] == row[next] or abs(row[x] - row[next]) == x - next: 
            return False
    return True
 
#한줄씩 재귀하며 dfs 실행
 
def dfs(x):
    global result
 
    if x == N:
        result += 1
    else:
        
        for i in range(N): # i 는 열번호 0부터 N 전까지 옮기면서 가정
            row[x] = i     # x번쨰 열 i번째 행에 퀸을 놓고 진행
            if Q_range(x): # 검사 시 가능하면
                dfs(x + 1) # 다음 열로 진행
 

N = int(input())
row = [0] * N
result = 0
dfs(0)
print(result)