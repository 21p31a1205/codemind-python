a=int(input())
b=int(input())
for j in range(a,b) :
    c=0
    if(j!=1):
         for i in range(2,j) :
             if(j%i==0):
                 c=1
         if(c==0) :
             print(j)