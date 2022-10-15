n=int(input())
l=list(map(int,input().split()))[:n]
z=int(input())
c=0
for i in l:
    if(i==z):
        c+=1
print(c)