n=int(input())
temp=n
sum=0
while(n>0):
    rem=n%10
    n//=10
    fact=1
    for i in range(1,rem+1):
        fact*=i
    sum+=fact
if(sum==temp):
    print("The number {} is a strong number".format(temp))
else:
    print("The number {} is not a strong number".format(temp))