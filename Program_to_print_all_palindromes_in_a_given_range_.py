def palindrome(n):
    temp=n
    s=0
    while(n):
        r=n%10
        s=s*10+r
        n=n//10
    if s==temp:
        return True
    else:
        return False
n=int(input())
m=int(input())
for i in range(n,m+1):
    if palindrome(i):
        print(i,end=" ")
        

        