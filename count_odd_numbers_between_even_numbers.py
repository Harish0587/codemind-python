n=int(input())
arr=list(map(int,input().split()))
s=0
for i in range(1,n-1):
    if arr[i]%2!=0 and arr[i-1]%2==0 and arr[i+1]%2==0:
        s=s+1
print(s)        