def lista(n):
    l=[]
    cont=[0,0]
    for i in range(n):
        l.append(int(input()))
    for i in l:
        if i>=10 and i<=20:
            cont[0]=cont[0]+1
        else:
            cont[1]=cont[1]+1
    return cont
while True:
    try:
        n=int(input())
        l=lista(n)
        print(l[0],"in")
        print(l[1],"out")
    except EOFError:
        break

