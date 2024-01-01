num = 123456*2
num_list =[1] *(num+1)
for i in range(2,num+1):
    for j in range(2, int(i**0.5)+1):
        if i % j ==0:
            num_list[i] =0
            break



while True:
    n = int(input())
    prime = 0
    if n==0:
        break
    
    for i in range(n+1,2*n+1):
        if num_list[i] ==1:
            prime+=1
    print(prime)



