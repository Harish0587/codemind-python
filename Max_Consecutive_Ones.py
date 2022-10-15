n=int(input())
l=list(map(int,input().split()))
c=0
k=0
for i in range(n):
    if l[i]==1:
        c+=1
        if(i==n-1):
            if(c>k):
                k=c
    elif(l[i]==0):
        if(c>k):
            k=c
        c=0
print(k)
