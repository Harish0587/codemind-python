n=int(input())
arr=list(map(int,input().split()))
c=[]
s=[]
for i in arr:
    if(i%2!=0):
        c.append(i)
    else:
        s.append(i)
x=c+s
print(*x)