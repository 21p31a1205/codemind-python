N,M=[int(x) for x in input().split()]
if N>M:
    smaller=M
else:
    smaller=N
for i in range(1,smaller+1):
    if N%i==0 and M%i==0:
        hcf=i
print(hcf)