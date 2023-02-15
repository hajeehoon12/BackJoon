def solution(numbers, hand):
    leftformat = "*"
    rightformat = "#"
    answer = ''
    
   
    def checkdistance(distance, k):
        a=0
        b=1
        c=2
        d=3
        e=4
        if k =="2":
            if distance == "2":
                return a
            if distance == "1" or distance =="3" or distance =="5":
                return b
            if distance == "4" or distance == "6" or distance == "8":
                return c
            if distance == "7" or distance =="0" or distance == "9":
                return d
            if distance == "*" or distance == "#":
                return e
        if k == "5":
            if distance == "5":
                return a
            if distance == "2" or distance =="4" or distance =="6" or distance =="8":
                return b
            if distance == "1" or distance == "3" or distance == "7" or distance =="9" or distance =="0":
                return c
            if distance == "*" or distance =="#":
                return d
        if k == "8":
            if distance == "8":
                return a
            if distance == "5" or distance =="7" or distance =="9" or distance =="0":
                return b
            if distance == "*" or distance == "#" or distance == "4" or distance =="6" or distance =="2":
               return c
            if distance == "1" or distance =="3":
                return d 
        if k == "0":
            if distance == "0":
                return a
            if distance == "*" or distance =="#" or distance =="8":
                return b
            if distance == "5" or distance == "7" or distance == "9":
                return c
            if distance == "2" or distance =="4" or distance == "6":
                return d
            if distance == "1" or distance == "3":
                return e

    
   
    for i in numbers:
        if i == "1" or i == "4" or i =="7" or i =="*":
            leftformat = i
            answer = answer + 'L'
        if i == "3" or i =="6" or i =="9" or i =="#":
            rightformat = i
            answer = answer + 'R'
        if i =="2" or i == "5" or i=="8" or i=="0":
            if hand == "right":
                m = checkdistance(leftformat,i)
                n = checkdistance(rightformat,i)
             
                if m>=n:
                    rightformat = i
                    answer = answer + 'R'
                else:
                    leftformat = i
                    answer = answer + 'L'
            if hand == "left":
                m = checkdistance(leftformat,i)
                n = checkdistance(rightformat,i)
                
                if m>n:
                    rightformat = i
                    answer = answer + 'R'
                else:
                    leftformat = i
                    answer = answer + 'L'
    
    return answer


