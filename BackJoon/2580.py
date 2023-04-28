import sys
graph = []
blank = []

for i in range(9):
    graph.append(list(map(int, sys.stdin.readline().rstrip().split())))

for i in range(9):
    for j in range(9):
        if graph[i][j] == 0:
            blank.append((i, j))

def checkRow(x, a): # 행 체크
    for i in range(9):
        if a == graph[x][i]:
            return False
    return True

def checkCol(y, a): # 열 체크
    for i in range(9):
        if a == graph[i][y]:
            return False
    return True

def checkRect(x, y, a): # 구역별 체크
    nx = x // 3 * 3
    ny = y // 3 * 3
    for i in range(3): 
        for j in range(3):
            if a == graph[nx+i][ny+j]:
                return False
    return True


def dfs(idx):
    if idx == len(blank):
        for i in range(9):
            print(*graph[i]) # 여기서 *은 리스트벗기기
        return(0)

    for i in range(1, 10): # 1~9까지 집어넣기
        x = blank[idx][0]
        y = blank[idx][1]

        if checkRow(x, i) and checkCol(y, i) and checkRect(x, y, i): # 3가지 조건 체크
            graph[x][y] = i # 만족하면 값 넣고
            dfs(idx+1)      # 다음 blank도 가정 진행
            graph[x][y] = 0 # 안쪽에서 못찾았을 경우 초기화
dfs(0)