def add(n):
    temp=n
    s=0
    while(temp>0):
        r=temp%10
        s=s+r
        temp=temp//10
    if s<=9:
        print(s)
    else:
        add(s)
n=int(input())
add(n)
        
        
        