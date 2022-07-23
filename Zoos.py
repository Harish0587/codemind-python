n=input()
c=0
d=0
for i in n:
    if i=='z':
        c=c+1
    if i=='o':
        d=d+1
if 2*c==d:
    print("Yes")
else:
    print("No")