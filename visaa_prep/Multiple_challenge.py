n=int(input())
divisible_3=n//3
divisible_5=n//5
divisible_both=n//(3*5)
multiples=divisible_3+divisible_5-divisible_both
print(multiples)
