n=int(input())
arr=list(map(int,input().split()))
c=0
p=0
for i in range(n):
    if arr[i]%2==0:
        c=c+1
    else:
        p=p+1 
print(c,p,end=' ')        