n=int(input())
if(n<60):
    print("0:0:{}".format(n))
elif(n>=60 and n<3600):
    n1,n2=n//60,n%60
    print("0:{m}:{s}".format(m=n1,s=n2))
elif(n>3600):
    n1,n2=n//3600,n%3600
    n3,n2=n2%60,n2//60
    print("{h}:{m}:{s}".format(h=n1,m=n2,s=n3))
