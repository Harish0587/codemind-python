n=int(input())
arr=list(map(int,input().split()))
l=[]
c=0
for i in arr:
    for j in arr:
        if i>j:
            c=c+1
    l.append(c)
    c=0
print(*l)    
        