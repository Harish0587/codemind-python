n=int(input())
arr=list(map(int,input().split()))
f=0
l=[]
for i in arr:
    if i==arr.count(i) and i not in l:
        l.append(i)
        f=1
if f==1:
    print(*l)
else:
    print("-1")