def isPrime(i):
    if(i==1 or i==0):
        return False
    for j in range(2,int(i**0.5)+1):
        if(i%j==0):
            return False
    return True

n=int(input())
for i in range(n):
    x=int(input())
    k=0
    while(1):
        if(isPrime(x-k)):
            break
        k+=1
    l=0
    while(1):
        if(isPrime(x+l)):
            break
        l+=1
    if(k==l):
         print(x-k)
    elif(k<l):
        print(x-k)
    else:
        print(x+l)