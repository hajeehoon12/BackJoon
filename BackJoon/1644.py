n = int(input())

a = [False, False] + [True] * (n-1) # 0~n 까지의 수를 표현 당연히 0,1은 제외
s_p = [] # sub_prime

for i in range(2, n+1): # 2~n 까지의 수를 검사
    if a[i]: # 아래서부터 검사하면서 소수가 참일 경우
        s_p.append(i) # 소수모음집에 추가하고
        for j in range(2*i, n+1, i): # 해당 소수의 배수부분을 전부 삭제
            a[j] = False

right, left = 0, 0 
ans = 0
sum = 0
#print(s_p)
while True:
    if right == len(s_p)+1:
        break
    if sum > n:
        sum -= s_p[left]
        left +=1
    elif sum ==n:
        ans +=1
        #print(right,left)
        sum -=s_p[left]
        left +=1    
    else:
        if right < len(s_p):
            sum += s_p[right]
            right +=1
        else:
            break
print(ans)
