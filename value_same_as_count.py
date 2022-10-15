n=int(input())
l1=[]
l=list(map(int,input().split()))
for i in l:
    if(i==l.count(i)):
        if i not in l1:
            l1.append(i)
print(len(l1))