import sys

n, c = map(int, sys.stdin.readline().split())
weight = list(map(int, sys.stdin.readline().split()))
aw = weight[:n//2]
bw = weight[n//2:]
asum = []
bsum = []

def bruteforce(arr, sumarr, l, value): # arr : 사용할 list , sumarr: 저장할 list , l = 현재 사용한 길이, value = 저장할 값
    if l >= len(arr): # warr 에 있는 array를 전부순회했을 때 종료
        sumarr.append(value)
        return
    bruteforce(arr, sumarr, l+1 , value) # 안더한 경우
    bruteforce(arr, sumarr, l+1 , value+arr[l]) # 더한 경우

def binaryserach(arr, target, start, end): # bsum 의 부분집합들에서 asum 의 부분집합들에 더할때 최적값 찾기
    while start < end:
        mid = ( start+ end ) // 2
        if arr[mid] <= target:
            start = mid + 1
        else:
            end = mid
    return end

bruteforce(aw, asum, 0 ,0) # 앞쪽 부분집합 구하기
bruteforce(bw, bsum, 0, 0) # 뒤쪽 부분집합 구하기

bsum.sort() # 뒤쪽 부분집합 정렬

cnt = 0
for i in asum:
    if c < i: # asum 에서 뽑아낸 값이 최대 무게 값보다 크면 볼 필요도 없음
        continue
    cnt += binaryserach(bsum, c-i, 0, len(bsum)) # bsum을 오름차순 정렬했기에 개수는 곧 end 의 값과 같음 
    #0~ end-1 까지의 array 의 개수 =end
print(cnt) 