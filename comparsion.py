a=int(input("enter a number for a:"))
b=int(input("enter a number for b:"))
choice= int(input("enter a number between 1-5 .1.add, 2.sub, 3.muliplication, 4.division, 5. floor divion"))
if choice==1:
    c=a+b
    print("addition",c)
elif choice==2:
    c=a-b
    print("sub",c)
elif choice==3:
    c=a*b
    print("multiplication",c)
elif choice==4:
    c=a/b
    print("division",c)
elif choice==5:
    c=a//b
    print("floor division",c)
else:
    print("invalid option")
