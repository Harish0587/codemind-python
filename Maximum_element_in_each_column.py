r,c=map(int,input().split())
l=[]
for i in range(r):
    arr=list(map(int,input().split()))[:c]
    l.append(arr)
for i in range(c):
    max=l[0][i]
    for j in range(r):
        if l[j][i]>max:
            max=l[j][i]
    print(max)        