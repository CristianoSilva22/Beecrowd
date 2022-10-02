v=int(input())
print("{}".format(v))
q100,q50,q20,q10,q5,q2,q1=0,0,0,0,0,0,0
while(v>0):
    if(v>=100):
        v-=100
        q100+=1
    elif(v>=50 and v<100):
        v-=50
        q50+=1
    elif(v>=20 and v<50):
        v-=20
        q20+=1
    elif(v>=10 and v<20):
        v-=10
        q10+=1
    elif(v>=5 and v<10):
        v-=5
        q5+=1
    elif(v>=2 and v<5):
        v-=2
        q2+=1
    else:
        v-=1
        q1+=1
print("{} nota(s) de R$ 100,00".format(q100))
print("{} nota(s) de R$ 50,00".format(q50))
print("{} nota(s) de R$ 20,00".format(q20))
print("{} nota(s) de R$ 10,00".format(q10))
print("{} nota(s) de R$ 5,00".format(q5))
print("{} nota(s) de R$ 2,00".format(q2))
print("{} nota(s) de R$ 1,00".format(q1))
        
