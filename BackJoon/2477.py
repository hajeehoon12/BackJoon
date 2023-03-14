import sys

mpl = int(sys.stdin.readline()) # 땅 per 참외 수

arr = [list(map(int,sys.stdin.readline().split())) for _ in range(6)]

w = 0 ; w_index =0 # 너비와 너비인덱스 초기화
h = 0 ; h_index =0 # 높이와 높이인덱스 초기화

for i in range(len(arr)):
    if arr[i][0] == 1 or arr[i][0] == 2: #dir이 가로면
        if w < arr[i][1]: # 여태 구한 최대보다 크면
            w = arr[i][1]
            w_index = i # 변경
    elif arr[i][0] == 3 or arr[i][0] == 4:                   # dir이 세로면
        if h< arr[i][1]: 
            h = arr[i][1]
            h_index = i # 변경

min_h = abs(arr[(w_index - 1 ) % 6][1] - arr[(w_index + 1) % 6][1] )
min_w = abs(arr[(h_index - 1 ) % 6][1] - arr[(h_index + 1) % 6][1] )

ans = ((w*h) - (min_h*min_w))*mpl
print(ans)