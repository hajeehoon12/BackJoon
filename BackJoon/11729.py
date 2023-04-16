
def hanoi(n, start, end) : # n개의 원판을 start지점에서 end 로 옮긴다.
    
    if n == 1 :
        print(start, end) # 출력
        
        return
       
    hanoi(n-1, start, 6-start-end) # 1단계
    print(start, end) # 2단계
    
    hanoi(n-1, 6-start-end, end) # 3단계
    
n = int(input())
print(2**n-1)
hanoi(n, 1, 3)