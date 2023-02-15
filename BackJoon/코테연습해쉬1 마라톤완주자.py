import collections

participant= ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]
test = ["leo", "eden","none"]

def solution(participant, completion):
    
    answer = collections.Counter(participant) - collections.Counter(completion)
    testanswer= collections.Counter(participant) - collections.Counter(test)
    print(answer)
    print(testanswer)
    return list(answer.keys())[0]
    #return list(answer.keys())[1]



print(solution(participant, completion))