n=int(input())
l=list(map(int,input().split()))[:n]
sum1=0
sum2=0
for i in range(n):
    if(l[i]%2==0):
        sum1+=l[i]
    else:
        sum2+=l[i]
print(abs(sum1-sum2))