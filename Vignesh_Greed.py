n=int(input())
arr=list(map(int,input().split()))
x=0
p=0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if arr[i]+arr[j]>arr[k] and arr[i]+arr[k]>arr[j] and arr[j]+arr[k]>arr[i]:
                p=arr[i]+arr[j]+arr[k]
                x=max(p,x)
if x>0:
    print(x)
else:
    print("-1")
