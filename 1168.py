n = int(input())
v = []
tl, c=0, 0
for i in range(n):
    v.append(input())
for i in range(n):
    for e in range(len(v[i])):
        c=v[i][e]
        if(c=="1"):
            tl=tl+2
        elif(c=="2" or c=="3" or c=="5"):
            tl=tl+5
        elif(c=="4"):
            tl=tl+4
        elif(c=="6" or c=="9" or c=="0"):
            tl=tl+6
        elif(c=="7"):
            tl=tl+3
        elif(c=="8"):
            tl=tl+7
    v[i]=tl
    e=0
    tl=0
for e in range(len(v)):
    print(v[e], "leds")
            
    
    
