n=int(input())
arr=list(map(int,input().split()))
k=int(input())
l=[]
f=0
for i in arr:
    if arr.count(i)==k and i not in l:
        l.append(i)
        f=1
if f==0:
    print("-1")
else:
    print(*l)