import sys

student_num = int(sys.stdin.readline())
student_list = []

for i in range(student_num):
    weight, height = map(int, sys.stdin.readline().split())  # 리스트에 맵형식으로 무게와 키를 넣고
    student_list.append((weight, height))

for i in student_list:
    rank = 1
    for j in student_list:
        if i[0] < j[0] and i[1] < j[1]:         # 비교이후 랭크측정
            rank +=1
    print(rank,end = " ")