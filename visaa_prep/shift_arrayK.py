n=int(input())
arr=list(map(int,input().split()))
k=int(input())
x=k%n
a=arr[-x:]+arr[:-x]
print(*a)
