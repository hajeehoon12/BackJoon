import sys
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj','s=','z=']

word = sys.stdin.readline().rstrip()

for i in croatia:
    word = word.replace(i, '*')
print(len(word))