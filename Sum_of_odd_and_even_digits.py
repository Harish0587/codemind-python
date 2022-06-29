n=int(input())
arr=list(map(int,input().split()))
s=0
k=0
for i in range(n):
    if i%2==0:
        s=s+arr[i]
    else:
        k=k+arr[i]
if  s-k==0:
    print("YES")
else:
    print("NO")
        