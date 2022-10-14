n=int(input())
sq=n*n
sum=0
while(sq>0):
    rem=sq%10
    sum+=rem
    sq//=10
if(sum==n):
    print("Neon Number")
else:
    print("Not Neon Number")