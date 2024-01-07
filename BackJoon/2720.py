n = int(input())

for i in range(n):
    m = int(input())
    a = m//25
    m -= a*25
    b = m//10
    m -= b* 10
    c = m//5
    m -= c * 5
    d = m
    print(a , b, c, d)