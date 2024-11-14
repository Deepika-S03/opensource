x,y,z=map(int,input().split())
weight=z-y
if weight>=0:
    mangoes=weight//x
else:
    mangoes=0
print(mangoes)
