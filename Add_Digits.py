
n=int(input())
while(n>=10):
    sum=0
    while(n>0):
        rem=n%10
        n//=10
        sum=sum+rem
    n=sum
print(n)