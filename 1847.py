d1,d2,d3=input().split()
d1,d2,d3=int(d1),int(d2),int(d3)
if(d1>d2 and d2<=d3):
    print(":)")
elif(d1<d2 and d2>=d3):
    print(":(")
elif(d1<d2 and d2<d3 and d2-d1>d3-d2):
    print(":(")
elif(d1<d2 and d2<d3 and d3-d2>=d2-d1):
    print(":)")
elif(d1>d2 and d2>d3 and d2-d3<d1-d2):
    print(":)")
elif(d1>d2 and d2>d3 and d1-d2<=d2-d3):
    print(":(")
elif(d1==d2):
    if(d2<d3):
        print(":)")
    else:
        print(":(")
