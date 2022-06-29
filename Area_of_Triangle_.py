A,B,C=[int(x) for x in input().split()]
s=(A+B+C)/2
area=(s*(s-A)*(s-B)*(s-C))**0.5
print("%.2f"%area)