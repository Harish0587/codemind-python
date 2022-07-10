n,k=map(int,input().split())
arr=list(map(int,input().split()))
c=0
for i in range(n):
    if arr[i]%k==0:
        c=c+1
print(c)        
