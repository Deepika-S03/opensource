n=int(input())
arr=list(map(int,input().split()))
repeated_once=2*sum(set(arr))-sum(arr)
print(repeated_once)
