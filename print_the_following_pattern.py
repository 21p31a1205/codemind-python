a=int(input())
for i in range(a):
  for j in range(a-i-1):
    print(" ",end="")
  for j in range(a):
    if i==0 or i==a-1:
       print("*",end="")
    else:
      if j==0 or j==a-1:
         print("*",end="")
      else:
        print(" ",end="")
  print("")