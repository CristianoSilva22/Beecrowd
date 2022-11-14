s=input()
n1,n2,n3,n4=s.split(" ")
n1,n2,n3,n4=float(n1),float(n2),float(n3),float(n4)
m=((n1*2)+(n2*3)+(n3*4)+n4)/10
print("Media: {:.1f}".format(m))
if(m>=7.0):
    print("Aluno aprovado.")
elif(m<5.0):
    print("Aluno reprovado.")
elif(m>=5.0 and m<=6.9):
    print("Aluno em exame.")
    avf=float(input())
    print("Nota do exame: {:.1f}".format(avf))
    m=(m+avf)/2
    if(m>=5.0):
        print("Aluno aprovado.\nMedia final: {:.1f}".format(m))
    elif(mf<=4.9):
        print("Aluno reprovado.\nMedia final: {:.1f}".format(m))
