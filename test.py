def s(n1,n2):
    if(n2!=0):
        print(n1,'=',n1//n2,'X',n2,'+',n1%n2)
        s(n2,n1%n2)
# n1,n2=int(input("enter a number: ")),int(input("enter a number: "))
n1=3768
n2=1701
s(n1,n2)
