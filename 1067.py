def lista(n):
    l=[]
    for i in range (1,n+1):
        if i%2!=0:
            l.append(i)
    return l
while True:
    try:
        v=int(input())
        l=lista(v)
        for i in l:
            print(i)
    except EOFError:
        break

