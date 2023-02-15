import sys
A = sys.stdin.readline().upper()

d = {}
for i in A:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1

a = []
for k,v in d.items():
    if v == max(d.values()):
        if not k =='\n' :
            a.append(k)
if len(a) ==1:
    print(a[0])
else:
    print('?')

