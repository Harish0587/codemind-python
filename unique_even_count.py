n=int(input())
arr=list(map(int,input().split()))
l=[]
c=0
for i in arr:
    if i not in l and i%2==0:
        l.append(i)
        c=c+1
print(c)