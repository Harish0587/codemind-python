n=int(input())
a1=0
a2=1
a=a1+a2
print(a1,a2,end=' ')
for i in range(3,n+1):
    print(a,end=' ')
    a1=a2
    a2=a
    a=a1+a2