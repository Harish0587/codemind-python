def prime(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    else:
        return True
n=int(input())
arr=list(map(int,input().split()))
m=int(input())
c=0
for i in arr:
    if prime(i) and i!=1:
        if i>=m:
            c=c+1
print(c)            