n=int(input())
arr=list(map(int,input().split()))
m=0
c=0
s=0
for i in arr:
    p=str(i)
    q=len(p)
    if q>=m:
        m=q
for i in arr:
    q=str(i)
    if len(q)==m:
        s=s+1
print(s)        