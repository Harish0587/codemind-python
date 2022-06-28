n=int(input())
s=0
square=n*n
while(square!=0):
    r=square%10
    s=s+r
    square=square//10
if s==n:
    print("Neon Number")
else:
    print("Not Neon Number")