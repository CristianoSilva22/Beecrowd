n=int(input())
for i in range(n):
    c=[0,0]
    l=input()
    for e in l:
        if(e=="<"):
            c[0]+=1
        elif(e==">"):
            if(c[0]>0):
                c[0]=c[0]-1
                c[1]+=1
    print(c[1])
