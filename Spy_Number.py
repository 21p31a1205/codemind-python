n=int(input())
sum,pro=0,1
while(n>0):
    rem=n%10
    sum+=rem
    pro*=rem
    n//=10
if(sum==pro):
    print("Spy Number")
else:
    print("Not Spy Number")