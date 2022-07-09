a,b,c=map(int,input().strip().split())
cap=2*a*b*c*512
d=cap//1024
t=str(d)
u=t+"KB"
print(u)