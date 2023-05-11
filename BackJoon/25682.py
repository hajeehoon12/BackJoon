import sys
input=sys.stdin.readline

def Chess(color):
    dp = [[0] * (M + 1) for i in range(N + 1)]
    for i in range(N):
        for j in range(M):
            if (i+j)%2==0:
                value=(L[i][j]!=color) # 참이면 value값 1 거짓이면 0
            else:
                value=(L[i][j]==color)
            dp[i+1][j+1]=dp[i][j+1]+dp[i+1][j]-dp[i][j]+value # 양 위 왼쪽단에서 값을가져옴
    count=int(1e9) # 반복횟수제한
    for i in range(1,N-K+2):
        for j in range(1,M-K+2):
            count=min(count,dp[i+K-1][j+K-1]-dp[i+K-1][j-1]-dp[i-1][j+K-1]+dp[i-1][j-1]) # 이전문제에서 한 것과 동일한 방식
    return count

N,M,K=map(int,input().split()) # N=세로 , M=가로 K= 최소크기

L=[]
for i in range(N):
    L.append(list(input().rstrip()))

print(min(Chess('W') , Chess('B'))) # W시작 B시작 중 최소 선택