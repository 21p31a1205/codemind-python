t=int(input())
for i in range(t):
    D,d,p,Q=map(int,input().split())
    n=D//d
    n1=D%d
    s=0
    for i in range(n):
        s+=(p+i*Q)*d;
    s+=(p+n*Q)*n1
    print(s)