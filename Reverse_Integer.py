n=int(input())
rev=0
f=0
while(n<0):
    n=n*-1
    f=1
while(n>0):
    r=n%10
    rev=rev*10+r
    n//=10
if f==1:
    print(rev*-1)
else:
    print(rev)