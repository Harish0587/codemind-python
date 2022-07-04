n=int(input())
arr=list(map(int,input().split()))
c=0
for i in range(n):
    if arr[i]%2!=0:
        c=i
print(c)        
        
        