n=int(input())
arr=list(map(int,input().split()))
for i in arr:
    if i<0:
        i=i*-1
    p=str(i)
    print(len(p),end=" ")
    