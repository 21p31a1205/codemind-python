n=input()
len1=len(str(n))
len2=len(set(n))
if len2==len1:
    print("Unique Number")
else:
    print("Not Unique Number")