n=int(input())
matrix=[]
for _ in range(n):
    x=list(map(int,input().split()))
    matrix.append(x)
for i in range(n):
    for j in range(n):
        print(matrix[j][i],end=" ")
    print()
