t=input()
c,v=t.split(" ")
c,v=int(c), int(v)
if(c==1):
    v=v*4.00
elif(c==2):
    v=v*4.50
elif(c==3):
    v=v*5.00
elif(c==4):
    v=v*2.00
elif(c==5):
    v=v*1.50
print("Total: R$ {:.2f}".format(v))
