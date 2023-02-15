import sys
t = int(sys.stdin.readline())
for i in range(t):
    n, m = map(int, sys.stdin.readline().split())
    s = list(map(int, sys.stdin.readline().split()))
    s_ = [0 for i in range(n)]        
    s_[m] = 1                       # 원하는 페이지인지 확인 1이 원하는페이지
    cnt = 0                          # 몇번째로 출력되는지 확인
    while True:
        if s[0] == max(s):
            cnt += 1
            if s_[0] == 1:
                print(cnt)
                break
            else:
                del s[0]
                del s_[0]
        else:
            s.append(s[0])
            del s[0]
            s_.append(s_[0])
            del s_[0]