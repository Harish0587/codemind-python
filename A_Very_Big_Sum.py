n=int(input())
arr=list(map(int,input().split()))
s=0
for i in range(n):
    s=s+arr[i]
print(s)    