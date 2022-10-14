def prime(a):
    c=0
    for i in range(1,a):
        if(a%i==0):
            c+=1
    if(c==1):
        return 1
    else:
        return 0
n=int(input())
v=0
for i in range(1,n+1):
    if(n%i==0 and prime(i)==0):
        v+=1
print(v)