import sys

numbers = sys.stdin.readline()
hand = sys.stdin.readline().strip()





def solution(numbers, hand):
    leftformat = "*"
    rightformat = "#"
    answer = ''

    def checkdistance(distance, k):

        if k ==2:
            if distance == "2":
                return 0
            if distance == "1" or distance =="3" or distance =="5":
                return 1
            if distance == "4" or distance == "6" or distance == "8":
                return 2
            if distance == "7" or distance =="0" or distance == "9":
                return 3
            if distance == "*" or distance == "#":
                return 4
        if k == 5:
            if distance == "5":
                return 0
            if distance == "2" or distance =="4" or distance =="6" or distance =="8":
                return 1
            if distance == "1" or distance == "3" or distance == "7" or distance =="9" or distance =="0":
                return 2
            if distance == "*" or distance =="#":
                return 3
        if k == 8:
            if distance == "8":
                return 0
            if distance == "5" or distance =="7" or distance =="9" or distance =="0":
                return 1
            if distance == "*" or distance == "#" or distance == "4" or distance =="6" or distance =="2":
               return 2
            if distance == "1" or distance =="3":
                return 3 
        if k == 0:
            if distance == "0":
                return 0
            if distance == "*" or distance =="#" or distance =="8":
                return 1
            if distance == "5" or distance == "7" or distance == "9":
                return 2
            if distance == "2" or distance =="4" or distance == "6":
                return 3
            if distance == "1" or distance == "3":
                return 4
   
    for i in numbers:
        if i == "[" or i =="]":
            answer = answer + '"'
        if i == "1" or i == "4" or i =="7" or i =="*":
            leftformat = "i"
            answer = answer + 'L'
        if i == "3" or i =="6" or i =="9" or i =="#":
            rightformat = "i"
            answer = answer + 'R'
        if i =="2" or i == "5" or i=="8" or i=="0":
            if hand == '"right"':
                if checkdistance(leftformat,i) >= checkdistance(rightformat,i):
                    rightformat = "i"
                    answer = answer + 'R'
                else:
                    leftformat = "i"
                    answer = answer + 'L'
            if hand == '"left"':
                if checkdistance(rightformat,i) >= checkdistance(leftformat,i):
                    leftformat = "i"
                    answer = answer + 'L'
                else:
                    rightformat = "i"
                    answer = answer + 'R'
            
    return answer


    

print(solution(numbers, hand))