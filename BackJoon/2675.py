import sys
t =int(sys.stdin.readline())
for i in range(t):
    num, s = sys.stdin.readline().split()
    text = ''
    for i in s:
        text += int(num) * i
    print(text)