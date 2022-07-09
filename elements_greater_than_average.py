n=int(input())
arr=list(map(int,input().split()))
s=0
c=0
for i in range(n):
    s=s+arr[i]
a=s//n
for i in range(n):
    if arr[i]>=a:
        c=c+1
print(c)        