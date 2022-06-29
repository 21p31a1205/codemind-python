X,Y=[int(x) for x in input().split()]
if(X==0 and Y%2==0):
    print("YES")
elif(X==0 and Y%2!=0):
    print("NO")
elif((X+2*Y)%2==0):
    print("YES")
else:
    print("NO")