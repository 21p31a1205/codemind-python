N=int(input())
for i in range(1,N+1):
    for j in range(1,N+1):
        if i==N or j==1 or i==j:
            print("*",end="")
        else:
            print(end=" ")
    print()