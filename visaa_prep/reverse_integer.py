n=int(input())
if n<0:
    s=-1
else:
    s=1
n=abs(n)
r=int(str(n)[::-1])*s
if (-2**31<=r) and r<=(2**31)-1:
    print(r)
else:
    print(0)
