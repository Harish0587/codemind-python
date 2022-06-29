n=int(input())
for i in range(n):
    a=int(input()) 
    rev=0
    temp=a
    while(a!=0):
        r=a%10
        rev=rev*10+r
        a=a//10
    if(temp==rev):
       print("True")
    else:
        print("False")