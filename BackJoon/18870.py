import sys

input = sys.stdin.readline
n = int(input())
location=list(map(int, input().split()))
sort_loc = sorted(set(location)) 

loc_dict = {sort_loc[i] : i for i in range(len(sort_loc))} # dictionary 저장방식

for loc in location:
    print(loc_dict[loc], end = ' ')