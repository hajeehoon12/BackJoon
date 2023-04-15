n = int(input())

six_count = 0
num = 0
while six_count <n:
    num +=1
    if '666' in str(num):
        six_count +=1
print(num)
