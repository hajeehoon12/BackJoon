from collections import deque

basedata = ['a', 'b', 'c', 'd']

dequedata = deque(basedata)

print("revers, rotate example")

dequedata.reverse()

print(dequedata)

dequedata.rotate()

print(dequedata)

dequedata.rotate(2)

print(dequedata)