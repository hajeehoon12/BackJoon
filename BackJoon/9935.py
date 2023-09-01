import sys

# 입력값 처리
S = sys.stdin.readline().rstrip()
bomb = sys.stdin.readline().rstrip()

# stack으로 문자열 폭발 구현
stack = []
num = len(bomb)

for i in range(len(S)):
    stack.append(S[i])
    #print(''.join(stack[-num:]))
    #print(bomb)
    if ''.join(stack[-num:]) == bomb:
        for _ in range(num):
            stack.pop()

# 결과 출력
if stack:
    print(''.join(stack))
else:
    print('FRULA')