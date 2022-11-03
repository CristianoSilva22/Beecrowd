n=int(input())
l=[]
c=1
for i in range(n):
    l.append(input())
for i in range(n):
    if(i<n-1):
        if(l[i]=="1"):
            if(l[i+1]=="2"):
                c+=1
        elif(l[i]=="2"):
            if(l[i+1]=="1"):
                c+=1
print(c)
