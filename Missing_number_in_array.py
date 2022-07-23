n=int(input())
for i in range(n):
    m=int(input())
    arr=list(map(int,input().split()))
    l=arr
    for i in range(m):
        i+=1
        if i not in l:
            print(i)