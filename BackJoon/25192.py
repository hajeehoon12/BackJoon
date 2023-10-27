n = int(input())
a = {}
result = 0
for _ in range(n):
    func = str(input())

    if func == "ENTER":
        result += len(a)
        a= {}
    else:
        if func not in a:
            a[func] =1

result += len(a)

print(result)