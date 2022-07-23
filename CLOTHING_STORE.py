n=int(input())
arr=list(map(int,input().split()))
q=set(arr)
c=0
for i in q:
    if arr.count(i)%2==0:
        c=c+(arr.count(i)//2)
    else:
        c=c+(arr.count(i)//2)
print(c)        