n=int(input())
arr=list(map(int,input().split()))
x=[]
for i in range(n):
    left_weight=sum(arr[:i])
    right_weight=sum(arr[i+1:])
    diff=abs(left_weight-right_weight)
    x.append(diff)
print(*x)
