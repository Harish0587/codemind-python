n=int(input())
arr=list(map(int,input().split()))
l=[]
for i in arr:
    if i not in l and i%2!=0:
        l.append(i)
l=sum(l)
print(l)