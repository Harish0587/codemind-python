def prime(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    else:
        return True
n=int(input())
c=1
for i in range(2,n+1):
    if n%i==0:
        if prime(i):
            continue
        else:
            c=c+1
print(c)            