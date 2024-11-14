t=int(input())
for i in range(0,t):
    X,N=map(int,input().split())
    score=N*(X//10)
    print(score)
