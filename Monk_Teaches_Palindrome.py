t=int(input())
for i in range(t):
    s=input()
    if(s==s[::-1]):
        if(len(s)%2==0):
            print("YES EVEN",end="
")
        else:
            print("YES ODD")
    else:
        print("NO")