n,m=map(int,input().split())
arr=list(map(int,input().split()))
s=0
for i in arr:
    if i<0:
        i=i*-1
    p=str(i)
    if len(p)==m:
        s=s+1
print(s)        