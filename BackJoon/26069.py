import sys
input = sys.stdin.readline
from collections import defaultdict

# 값이 주어지지 않으면 bool 형태의 false로 초기화 
dance = defaultdict(bool) 
# 총총이만 춤을 추고있으므로 True로 초기화
dance['ChongChong'] = True
answer = 1

for _ in range(int(input())):
    # A와 B가 만났다.
    A, B = input().split()
    # 두 사람 중 한 사람만 추고 있다면
    # 추고 있지 않은 사람을 추게 만들면 된다.
    if dance[A]:
        if not dance[B]:
            dance[B] = True
            answer += 1
    elif dance[B]:
        dance[A] = True
        answer += 1

print(answer)