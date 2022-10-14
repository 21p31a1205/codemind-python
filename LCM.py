a,b=map(int,input().split())
m=max(a,b)
for i in range(1,m+1):
    if((m*i)%a==0 and (m*i)%b==0):
        print(m*i)
        break