def isprime(i):
    if(i==1 or i==0):
        return False
    else:
        for j in range(2,int(i**0.5)+1):
            if(i%j==0):
                return False
        return True

a=int(input())
b=int(input())
for i in range(a,b+1):
    if(isprime(i)):
        print(i)
        