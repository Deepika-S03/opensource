x,n=map(int,input().split())
passengers=x*100
if n>passengers:
    remaining=n-passengers
    if remaining%100==0:
        planes=remaining//100
    else:
        planes=remaining//100+1
else:
    planes=0
print(planes)
