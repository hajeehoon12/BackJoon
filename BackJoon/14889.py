import sys
from itertools import combinations #조합 함수

N = int(sys.stdin.readline()) # 주어지는 맴버 수
S = [list(map(int, sys.stdin.readline().split())) for _ in range(N)] # 표
members = [i for i in range(N)] # 주어진 맴버 네이밍
possible_team = []  # 가능한팀들 list

#조합으로 가능한 팀 생성해주기
for team in list(combinations(members, N//2)):
    possible_team.append(team)

min_stat_gap = 10000 #갭이 가장 작은 값을 찾기 위하여
for i in range(len(possible_team)//2):         # 조합의 경우 절반까지고 나머지는 중복되기에
    #A 팀
    team = possible_team[i]
    stat_A = 0 #A팀 능력치
    for j in range(N//2):
        member = team[j] #멤버
        for k in team:
            stat_A += S[member][k] #멤버와 함께할 경우의 능력치들 # 자기자신은 다 0이기에 포함해도 상관없음
            
    #A를 제외한 나머지 팀
    team = possible_team[-i-1]       # 위의 조합과 반대기에 남는 사람
    stat_B = 0
    for j in range(N//2):
        member = team[j]
        for k in team:
            stat_B += S[member][k]
            
    min_stat_gap = min(min_stat_gap, abs(stat_A - stat_B))
    
print(min_stat_gap)