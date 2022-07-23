n=int(input())
arr=list(map(int,input().split()))
c=0
for i in range(n):
    l=len(str(arr[i]))
    if l%2==0:
        c=c+1
print(c)        