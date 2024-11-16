n=int(input())
matrix=[]
for i in range(n):
    x=list(map(int,input().split()))
    matrix.append(x)
for i in range(n):
    for j in range(n-1,-1,-1):
        print(matrix[i][j],end=" ")
    print()
