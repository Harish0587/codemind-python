def palindrome(x):
    temp=x
    s=0
    while(x):
        r=x%10
        s=s*10+r
        x=x//10
    if temp==s:
        return True
    else:
        return False
    
x=int(input()) # 95
st=str(x) 
s=x+int(st[::-1])
while(True):
    if(palindrome(s)):
        print(s)
        break
    t=str(s)
    s=s+int(t[::-1])
