import sys
p = sys.stdin.readline()



def circulation(temp2,temp3):
        k = len(temp2)
        resulted = ""
        free = ""
        if k==0:
            return
        
        if k==2:
            return "()"
            
        temp2 = temp2[1:k-1]
        for j in temp2:
            if j == "(":
                free= free +")"
            if j == ")":
                free= free + "("
           
                
       
        resulted = "(" + solution(temp3)  + ")" + free 
            
        return resulted


def solution(p):
    temp = "" 
    answer = ""
    amount = 0

    for i in p:
        lenofp = len(p)
        if i == "(":
            temp= temp + i
            amount +=1
            if amount ==0: 
                temp3 = p[len(temp)+1:lenofp]
                answer = answer + circulation(temp,temp3)
                temp = ""
                
        if i == ")":
            temp= temp + i
            amount -=1
            if amount ==0:
                for s in temp:
                    answer = answer+ s
                    
                    p = p[len(temp)+1:lenofp]
                    
                    solution(p)
        
        
    return answer

print(solution(p))