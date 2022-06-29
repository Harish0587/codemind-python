n=int(input())
arr=list(map(int,input().split()))
c=0
k=0
for i in range(n):
    if i%2==0 and arr[i]%2==0:
        c=c+1
for i in range(n):
    if arr[i]%2==0:
        k=k+1
if c==k:
    print("True")
else:
    print("False")
        
        
        
        
        
        