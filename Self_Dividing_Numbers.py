def sel(n):
    c=0
    for i in str(n):
        if int(i)!=0:
            if n%int(i)==0:
                c+=1
    if c==len(str(n)):
        return True
    else:
        return False
n=int(input())
m=int(input())
for i in range(n,m+1):
    if sel(i):
        print(i,end=" ")