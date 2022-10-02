a,b,c=input().split(" ")
a,b,c=float(a),float(b),float(c)
tri=(a*c)/2
cir=3.14159*(c*c)
tra=((a+b)*c)/2
qua=b**2
ret=a*b
print("TRIANGULO: {tr:.3f}\nCIRCULO: {ci:.3f}\nTRAPEZIO: {trap:.3f}\nQUADRADO: {qu:.3f}\nRETANGULO: {re:.3f}".format(tr=tri,ci=cir,trap=tra,qu=qua,re=ret))
