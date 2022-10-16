n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    arr=list(map(int,input().split()))
    for j in range(b):
        f=arr[-1]
        arr.insert(0,f)
        arr.pop()
    print(*arr)    