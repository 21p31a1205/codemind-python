a=int(input())
b=int(input())

for i in range(a,b+1) :
    v=0
    t=i 
    while i!=0 :
         r=i%10
         v=v*10+r
         i=i//10
         if(v==t):
            print(v,end =" "),
            