def palindrome(n):
    rev=0
    temp=n
    while(n!=0):
        r=n%10
        rev=rev*10+r
        n=n//10
    if temp==rev:
        return True
    else:
        return False
n=int(input())
arr=list(map(int,input().split()))
c=0
for i in arr:
    if palindrome(i):
        c=c+1
print(c)        