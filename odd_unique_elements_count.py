n=int(input())
arr=list(map(int,input().split()))
r=[]
c=0
for i in arr:
    if i not in r and i%2!=0:
        r.append(i)
        c+=1
print(c)        