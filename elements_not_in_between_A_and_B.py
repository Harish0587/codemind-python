n=int(input())
arr=list(map(int,input().split()))
a,b=map(int,input().split())
l=[]
for i in range(n):
    if arr[i]<a or arr[i]>b not in l:
        l.append(arr[i])
if len(l)==0:
    print("-1")
else:
    print(*l)