n=int(input())
while(n>9):
    sum=0
    while(n>0):
        rem=n%10
        sum+=rem
        n//=10
    n=sum
print(n)