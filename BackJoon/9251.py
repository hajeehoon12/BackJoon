import sys
input = sys.stdin.readline

word_1 = input().rstrip()
word_2 = input().rstrip()

h,w = len(word_1), len(word_2)

cache = [[0] * (w+1) for _ in range(h+1)]

for i in range(1, h+1):
    for j in range(1, w+1):
        if word_1[i-1] == word_2[j-1]:
            cache[i][j] = cache[i-1][j-1] + 1
        else:
            cache[i][j] = max(cache[i][j-1], cache[i-1][j])
print(cache[h][w])