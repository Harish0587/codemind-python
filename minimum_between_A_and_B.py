n=int(input())
arr=list(map(int,input().split()))
a,b=map(int,input().split())
l=[]
f=0
for i in range(a,b+1):
    if i in arr:
        l.append(i)
        f=1
if f==1:
    print(min(l))
else:
    print("-1")