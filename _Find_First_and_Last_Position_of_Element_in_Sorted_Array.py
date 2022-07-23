n=int(input())
arr=list(map(int,input().split()))
m=int(input())
arr.sort()
l=[]
for i in range(len(arr)):
    if m==arr[i]:
        l.append(i)
if len(l)==0:
    print("-1 -1")
else:
    print(l[0],l[-1])