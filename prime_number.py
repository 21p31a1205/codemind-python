def prime(m):
    if m<=2:
        return 0
    for i in range(2,int(m**0.5)+1):
        if (m%i==0):
            return 0
    return 1
n=int(input())
if prime(n):
    print("prime")
else:
    print("not a prime")
    