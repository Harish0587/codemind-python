n=int(input())
arr=list(map(int,input().split()))
l=[]
c=0
for i in arr:
    if i==arr.count(i) and i not in l:
        l.append(i)
        f=1
        c=c+1
print(c)