t=int(input())
for i in range(t):
  a=int(input())
  arr=list(map(int,input().split()))
  if a==0:
     print(0)
  else:
    ar=[]
    for j in arr:
      if j in range(1,1000000000,2):
         ar.append(j)
    if len(ar)==1:
       print(0)
    elif len(ar)%2==0:
       print(len(ar)//2)
    else:
      print((len(ar)-1)//2)