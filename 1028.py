def mdc(a, b):
    resto = None
    while resto != 0:
        resto = a % b
        a = b
        b = resto
    return a
c=int(input())
for i in range(c):
    f1,f2=input().split(" ")
    r=mdc(int(f1),int(f2))
    print(r)
