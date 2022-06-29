N=int(input())
for i in range(1,N+1):
    for j in range(1,N+1):
        if(i==j):
            print("0",end="")
        else:
            print("x",end="")
    print()