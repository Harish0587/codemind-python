n=int(input()) 
arr=list(map(int,input().strip().split()))[:n]
c=0
hcf=0
q=min(arr)
for i in range(1,q+1):
    for j in range(n):
       if arr[j]%i==0:
          c+=1
    if(c==len(arr)):
        hcf=i
    c=0    
print(hcf)    