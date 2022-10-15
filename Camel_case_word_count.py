s=input()
c=0
l="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in s:
    if i in l :
        c+=1
if s[0] not in l:
    c+=1
print(c)