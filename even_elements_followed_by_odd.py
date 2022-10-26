n=int(input())
arr=list(map(int,input().split()))
l=[]
s=[]
for i in arr:
    if i%2==0:
        l.append(i)
    else:
        s.append(i)
c=l+s
print(*c)