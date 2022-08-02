n=input()
s=n.split()
c=0
t=0
for i in s:
    minu=ord(min(i))
    c=c+minu
for i in s:
    maxi=ord(max(i))
    t=t+maxi
print(t-c)    