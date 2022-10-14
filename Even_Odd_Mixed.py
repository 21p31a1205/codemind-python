n=int(input())
c=d=0
while n>0:
    r=n%10
    if(r%2==0):
        c+=1
    else:
        d+=1
    n=n//10
if(c==0 and d!=0):
    print("Odd")
elif(c!=0 and d!=0):
    print("Mixed")
else:
    print("Even")