n=int(input())
m=int(input())
for i in range(n,m+1):
    if "0" not in str(i):
        flag=1
        for j in str(i):
            if(i%int(j)!=0):
                flag=0
        if(flag==1):
            print(i,end=" ")