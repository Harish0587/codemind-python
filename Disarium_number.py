import math
n=int(input())
s=0
c=0
temp=n
while(temp!=0):
    temp=temp//10
    c+=1
temp=n
while(temp!=0):
    r=temp%10
    s=s+pow(r,c)
    temp=temp//10
    c-=1
if(s==n):
    print("True")
else:
    print("False")