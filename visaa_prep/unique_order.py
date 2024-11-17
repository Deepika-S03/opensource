n=int(input())
arr=list(map(int,input().split()))
x=[]
for i in arr:
    if i not in x:
        x.append(i)
print(*x)
