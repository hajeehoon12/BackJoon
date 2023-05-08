import sys
input = sys.stdin.readline

s = input().rstrip()

q = int(input())

arr  = [[0 for i in range(26)] for i in range(len(s))]

arr[0][ord(s[0]) -97] = 1 # 알파벳 첫 공간에 값 1을 초기화시켜줌

def ordlang(i,s):
    return ord(s[i]) - 97

for i in range(1, len(s)):
    arr[i][ordlang(i,s)] = 1
    for j in range(26):
        arr[i][j] += arr[i-1][j]

for i in range(q):
    a= input().rstrip().split()
    temp = ordlang(0,a)

    if int(a[1]) > 0:
        result = arr[int(a[2])][temp] - arr[int(a[1])-1][temp]
    else:
        result = arr[int(a[2])][temp]
    print(result)