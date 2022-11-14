s=input()
p1,p2=s.split(" ")
p1,p2=float(p1),float(p2)
if(p1>0):
    if(p2>0):
        print("Q1")
    elif(p2<0):
        print("Q4")
    elif(p2==0):
        print("Eixo X")
elif(p1<0):
    if(p2>0):
        print("Q2")
    elif(p2<0):
        print("Q3")
    elif(p2==0):
        print("Eixo X")
elif(p1==0):
    if(p2==0):
        print("Origem")
    else:
        print("Eixo Y")
