s=input()
a,b,c=s.split(" ")
a,b,c=float(a),float(b),float(c)
delta=(b**2)-(4*(a*c))
if(delta<0 or a==0):
    print("Impossivel calcular")
else:
    r1=(-b+(delta**0.5))/(2*a)
    r2=(-b-(delta**0.5))/(2*a)
    print("R1 = {ra1:.5f}\nR2 = {ra2:.5f}".format(ra1=r1,ra2=r2))
