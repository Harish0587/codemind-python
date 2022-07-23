n=int(input())
arr=list(map(int,input().split()))
q=set(arr)
for i in q:
    if arr.count(i)>n//2:
        print(i)