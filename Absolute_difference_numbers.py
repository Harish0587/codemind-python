n,x=map(int,input().split())
q=str(n)
arr=list(q)
c=0
s=0
for i in range(x):
    s=s*10+int(arr[i])
for i in range(-x,0,1):
    c=c*10+int(arr[i])
print(abs(s-c))

    