n=int(input())
for i in range(n):
    s=input()
    for i in s:
        if(i.isdigit()):
            print("Yes")
            break
    else:
        print("No")