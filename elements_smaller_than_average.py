n=int(input())
arr=list(map(int,input().split()))
s=0
c=0
for i in arr:
    s=s+i
avg=s/n
for i in arr:
    if avg>=i:
        c=c+1
print(c)        