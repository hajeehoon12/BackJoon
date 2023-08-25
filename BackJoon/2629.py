import sys

input = sys.stdin.readline

ball_num = int(input())

ball = list(map(int , input().split()))

#print(ball)

weight_num = int(input())

weight_ball = list(map(int, input().split()))
                
#print(ans_ball)

dp, ans = [[0 for _ in range((i+1)*500)] for i in range(ball_num+1)], []

def cal(num, weight):

    if num > ball_num:
        return
    
    if dp[num][weight]:
        return
    
    dp[num][weight] = 1

    cal(num+1 , weight)
    cal(num+1, weight + ball[num-1])
    cal(num+1, abs(weight - ball[num-1]))

cal(0,0)

for i in weight_ball:
    if i > 30 *500:
        ans.append("N")
        continue
    if i < 0:
        ans.append("N")
        continue
    if dp[ball_num][i] == 1:
        ans.append("Y")
    else:
        ans.append("N")
print(*ans)