from collections import deque

basedata = ['a', 'b', 'c', 'd']

dequedata = deque(basedata)
dequedata1 = deque([1,2,3,4])
print(dequedata)
print(dequedata1)

dequedata = deque(basedata, maxlen=3)
print(dequedata)


