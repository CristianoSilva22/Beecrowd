import math
s=input().split(" ")
a,b,c=s
a,b,c=int(a),int(b),int(c)
mab=int((a+b+abs(a-b))/2)
r=int((mab+c+abs(mab-c))/2)
print("{} eh o maior".format(r))
