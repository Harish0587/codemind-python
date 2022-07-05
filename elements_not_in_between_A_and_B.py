n=int(input())
arr=list(map(int,input().split()))
a,b=map(int,input().split())
f=0
for i in arr:
    if i<a or i>b:
        print(i,end=" ")
        f=1
if f==0:
    print("-1")
      