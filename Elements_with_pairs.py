n=int(input())
arr=list(map(int,input().split()))
if n%2==0:
    for i in arr:
        print(i,end=' ')
else:
    arr.append(0)
    for i in arr:
        print(i,end=' ')