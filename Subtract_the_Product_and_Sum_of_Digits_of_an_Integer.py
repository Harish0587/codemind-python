n=int(input())
Sum=0
Pro=1
while(n>0):
    r=n%10
    Sum=Sum+r
    Pro=Pro*r
    n=n//10
m=Pro-Sum
print(m)
    