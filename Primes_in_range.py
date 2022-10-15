def isPrime(i):
    if i==1:
        return False
    for j in range(2,int(i**0.5)+1):
        if(i%j==0):
            return False
    return True

c=0
n=int(input())
m=int(input())
for i in range(n,m+1):
    if(isPrime(i)):
        c+=1
print(c)