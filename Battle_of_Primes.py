n1=int(input())
n2=int(input())
s=0
t=0
s=n1+n2
for i in range(1,s):
    t=s+i
    c=0
    for j in range(2,t):
        if(t%j==0):
            c=c+1
    if(c==0):
        print(i)
        break