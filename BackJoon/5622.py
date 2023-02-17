import sys
alpha_list = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
word = sys.stdin.readline()

time = 0 

for i in word:
    for unit in alpha_list:
        for e in unit:
            if i == e:
                time += alpha_list.index(unit)+3
print(time)