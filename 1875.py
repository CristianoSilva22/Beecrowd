c=int(input())
for i in range(c):
    p=int(input())
    l=[0,0,0]
    for e in range(p):
        t=input().split(" ")
        if(t[0]=="R"):
            if(t[1]=="B"):
                l[0]+=1
            elif(t[1]=="G"):
                l[0]+=2
        elif(t[0]=="B"):
            if(t[1]=="G"):
                l[1]+=1
            elif(t[1]=="R"):
                l[1]+=2
        elif(t[0]=="G"):
            if(t[1]=="R"):
                l[2]+=1
            elif(t[1]=="B"):
                l[2]+=2
    if(l[0]==l[1] and l[1]==l[2]):
        print("trempate")
    elif(l[0]>l[1] and l[0]>l[2]):
        print("red")
    elif(l[1]>l[0] and l[1]>l[2]):
        print("blue")
    elif(l[2]>l[0] and l[2]>l[1]):
        print("green")
    else:
        if(l[0]==l[1] and l[0]>l[2]):
            print("empate")
        elif(l[0]==l[2] and l[0]>l[1]):
            print("empate")
        elif(l[1]==l[2] and l[1]>l[0]):
            print("empate")
