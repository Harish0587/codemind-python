n=int(input())
arr=list(map(int,input().split()))
s=0
for i in range(n):
    if arr[i]%2!=0:
        s=arr[i]
print(s)        