n=int(input())
temp=n
rev=0
while(temp):
    r=temp%10
    rev=rev*10+r
    temp=temp//10
print(rev)    
    