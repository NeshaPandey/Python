T=int(input("enter term"))
t1,t2=0,1
c=0
if T<0:
    print("Invalid")
elif T==1:
    print(t1)
elif T==2:
    print(t1,t2)
else:
    while c<T:
        print(t1)
        nth=t1+t2
        t1=t2
        t2=nth
        c+=1
