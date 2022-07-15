a=int(input())
lst=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
for i in range(a,0,-1):
  for j in range(i):
    print(lst[i-1],end=" ")
  print("")