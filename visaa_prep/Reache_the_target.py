n=int(input())
for i in range(n):
    x,y=map(int,input().split())
    runs=x-y+1
    print(runs)
