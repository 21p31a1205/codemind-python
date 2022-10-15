n=int(input())
l=list(map(int,input().split()))
sum=0
for i in range(n):
    if(l[i]%2==1):
        sum+=l[i]
print(sum)