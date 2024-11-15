n=input()
count=1
s=''
for i in range(1,len(n)):
    if n[i]==n[i-1]:
        count+=1
    else:
        s+=n[i-1]+str(count)
        count=1
s+=n[-1]+str(count)
print(s)
