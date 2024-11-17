n=int(input())
arr=list(map(int,input().split()))
x=arr[0]
y=[]
for i in range(1,n):
    y.append(arr[i])
y.append(x)
print(*y)
