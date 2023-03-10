import sys

_ = sys.stdin.readline()
N = sorted(map(int,sys.stdin.readline().split()))
_ = sys.stdin.readline()
M = map(int, sys.stdin.readline().split())

def binary(n, N, start, end):
    if start > end:
        return 0
    m = (start+end)//2
    if n == N[m]:
        return N[start:end+1].count(n)
    elif n < N[m]:
        return binary(n,N, start, m-1)
    else:
        return binary(n,N,m+1,end)

n_dic = {}
for n in N:
    start = 0
    end = len(N) - 1
    if n not in n_dic:
        n_dic[n] = binary(n, N, start, end)
for i in M:
    if i not in n_dic:
        print(0, end = " ")
        continue
    print(n_dic[i],end = " " )
   

