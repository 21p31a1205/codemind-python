a,b=map(int,input().split())
m=max(a,b)
for i in range(1,m):
    if(a%i==0 and b%i==0):
        r=i
print(r)