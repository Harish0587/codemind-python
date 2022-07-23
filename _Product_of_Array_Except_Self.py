n=int(input())
arr=list(map(int,input().split()))
p=1
for i in arr:
    for j in arr:
        if i==j:
            continue
        else:
            p=p*j
    print(p,end=' ')
    p=1