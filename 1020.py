n=int(input())
if(n<30):
    print("0 ano(s)\n0 mes(es)\n{} dia(s)".format(n))
elif(n>=30 and n<365):
    n1,n2=n//30,n%30
    print("0 ano(s)\n{m} mes(es)\n{d} dia(s)".format(m=n1,d=n2))
elif(n>=365):
    n1,n2=n//365,n%365
    n3,n2=n2%30,n2//30
    print("{a} ano(s)\n{m} mes(es)\n{d} dia(s)".format(a=n1,m=n2,d=n3))
