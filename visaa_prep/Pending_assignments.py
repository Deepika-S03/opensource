x,y,z=map(int,input().split())
total_time=z*24*60
time_needed=x*y
if total_time>=time_needed:
    print("YES")
else:
    print("NO")
