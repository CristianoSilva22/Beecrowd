o=input()
c=0
l=[]
for i in range(12):
    a = []
    for j in range(12):
        a.append(float(input()))
    l.append(a[:])
    
for i in range(1,6):
    for j in range(11, 11-i,-1):
        c += l[i][j]

for i in range(6,12):
    for j in range(i+1, 12):
        c += l[i][j]
            
if(o=="M"):
    print("{:.1f}".format(c/144))
elif(o=="S"):
    print("{:.1f}".format(c))