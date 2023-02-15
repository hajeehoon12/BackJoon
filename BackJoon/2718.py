import sys
A=[] ## 결과
B=[]  #23번케이스
C=[]   # 45 번케이스

A.append(1)
A.append(5)
B.append(1)
B.append(1)
C.append(1)
C.append(2)
K= []
P =[]
N = int(sys.stdin.readline())
for n in range(N):
    t=sys.stdin.readline().strip()
    K.append(int(t))
P=sorted(K)

x = int(P[N-1])
for n in range(2,x+1):

    A.append(int(A[n-2]+A[n-1]+B[n-1]+2*C[n-1]))
    B.append(int(B[n-2]+A[n-1]))
    C.append(int(C[n-1]+A[n-1]))

for i in K:
    print(A[i-1])

