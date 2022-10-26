n=int(input())
arr=list(map(int,input().split()))
a=int(input())
f=0
for i in range(n):
    if arr[i]==a:
        f=1
if f==1:
    print("True")
else:
    print("False")