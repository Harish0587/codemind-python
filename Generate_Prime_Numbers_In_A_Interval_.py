n=int(input())
m=int(input())
count=0
f=0
if(n==1 or n<0):
    n=2
for i in range(n,m+1):
    for j in range(2,i):
        if(i%j==0):
            f=1
            break
    if(f==0):
        print(i)
    f=0    