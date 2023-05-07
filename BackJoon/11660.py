import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

rect = []


for i in range(n):
    temp = list(map(int , input().rstrip().split()))
    rect.append(temp)

ans = [] 

for i in range(m):
    x1,y1,x2,y2 = map(int, input().rstrip().split())
    ans.append([x1,y1,x2,y2])

#print(rect)
#print(ans)

def sum_rect(x1,y1,x2,y2):
    sum = 0
    for j in range(x1-1,x2):
        for k in range(y1-1,y2):
            sum += rect[j][k]
    return sum



for i in ans:
    x1,y1,x2,y2 = i
    temp_ans = sum_rect(x1,y1,x2,y2)
    
    print(temp_ans)