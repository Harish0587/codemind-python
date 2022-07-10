n=int(input())
arr=list(map(int,input().split()))
a,b=map(int,input().split())
f=0
for i in range(n):
    if arr[i]>=a and arr[i]<=b:
        print(arr[i],end=" ")
        f=1
if f==0:
    print("-1")