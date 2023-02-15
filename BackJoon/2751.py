import sys

n=int(sys.stdin.readline())
outcome = []
for i in range(n):
    m = int(sys.stdin.readline().strip())
    outcome.append(m)
    
outcome = sorted(outcome)

for i in range(n):

    print(outcome[i])


