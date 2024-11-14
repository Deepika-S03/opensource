n=int(input())
digit_sum=0
while(n!=0):
    r=n%10
    digit_sum+=r
    n=n//10
if digit_sum%2==0:
    print("Vignesh")
else:
    print("Charan")
