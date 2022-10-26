n=int(input())
arr=list(map(int,input().split()))
l=[]
for i in range(n):
    if arr[i]%2==0:
        l.append(i)
if len(l)==n:
    print("True")
else:
    print("False")
        