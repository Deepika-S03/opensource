n=int(input())
arr=[]
for i in range(n):
    x,y=map(int,input().split())
    m=x//10
    points=m*y
    arr.append(points)
for i in arr:
    print(i)
