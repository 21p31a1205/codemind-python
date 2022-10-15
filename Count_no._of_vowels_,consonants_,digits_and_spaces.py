s=input()
c1,c2,c3,c4=0,0,0,0
s=s.lower()
v="aeiou"
C="bcdfghjklmnpqrstvwxyz"
l1,l2,l3=[],[],[]
for i in s:
    if i!=' ':
        if i in v:
            c1+=1
        elif i in C:
            c2+=1
        else:
            c3+=1
    else:
        c4+=1
print("Vowels:",c1)
print("Consonants:",c2)
print("Digits:",c3)
print("White spaces:",c4)