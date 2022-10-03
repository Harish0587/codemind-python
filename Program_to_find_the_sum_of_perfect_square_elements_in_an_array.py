n=int(input())
arr=list(map(int,input().split()))
s=0
for i in arr:
    if(i==1):
        s=s+i
    else:
        for j in range(i//2+1):
            if(i==j*j):
                s+=i
print(s)                