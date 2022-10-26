n=int(input())
arr=list(map(int,input().strip().split()))
z=int(input())
c=0
for i in arr:
    if z==i:
        c=c+1
print(c)        