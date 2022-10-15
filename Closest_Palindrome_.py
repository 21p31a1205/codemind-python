def isPalindrome(i):
    temp=i
    rev=0
    while(temp>0):
        rev=rev*10+temp%10
        temp//=10
    if(i==rev):
        return True
    else:
        return False
x=int(input())
k=1
while(1):
    if(isPalindrome(x-k)):
        break
    k+=1
l=1
while(1):
    if(isPalindrome(x+l)):
        break
    l+=1
if(k==l):
         print(x-k,x+l)
elif(k<l):
        print(x-k)
else:
        print(x+l)