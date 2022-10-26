n=int(input())
arr=list(map(int,input().split()))
a,b=map(int,input().split())
l=[]
#print(arr)
#print(a,b)
for i in arr:
    if(i<a or i>b):
        l.append(i)
if(len(l)==0):
    print("-1")
else:
    print(min(l))