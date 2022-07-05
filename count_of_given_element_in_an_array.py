n=int(input())
arr=list(map(int,input().split()))
x=int(input())
c=0
for i in arr:
    if i==x:
        c+=1
print(c)