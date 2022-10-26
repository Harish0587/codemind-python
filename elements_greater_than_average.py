n=int(input())
arr=list(map(int,input().split()))
c=0
s=0
for i in arr:
    s=s+i
avg=s//n
for i in arr:
    if i>=avg:
        c+=1
print(c)        