n=int(input())
arr=list(map(int,input().split()))
s=0
r=[]
for i in arr:
    if i not in r:
        r.append(i)
r=sum(r)
print(r)