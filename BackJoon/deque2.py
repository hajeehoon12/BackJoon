from collections import deque

basedata = ['a', 'b', 'c', 'd']

dequedata = deque(basedata)

print("pop/popleft example")

dequedata.pop()

print(dequedata)

dequedata.popleft()

print(dequedata)

basedata = ['a', 'b', 'c', 'd']

dequedata = deque(basedata)

print("remove, clear example")

dequedata.remove('a')

print(dequedata)

dequedata.clear()

print(dequedata)