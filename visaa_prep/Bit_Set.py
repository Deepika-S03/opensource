n=int(input())
k=int(input())
B=str(0*k)+bin(n)[2:]
if len(B)>=k and B[-k]=="1":
       print("true")
else:
       print("false")
