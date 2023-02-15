from collections import deque

basedata = ['a','b','c','d']
sampleData = ['z','k','e','r']
dequedata = deque(basedata)
print("append example")
dequedata.append('e')
print(dequedata)
dequedata.appendleft('z')
print(dequedata)

basedata = ['a','b','c','d']
sampleData = ['z','k','e','r']

print("extend example")
dequedata.extend(sampleData)
print(dequedata)
dequedata = deque(basedata)
dequedata.extendleft(sampleData)
print(dequedata)