a=[]
b=int(input("enter the length of list"))
for j in range(0,b):
    c=int(input("enter the element for list"))
    a.append(c)
for i in a:
    if i >= 0:
       print(i, end = " ") 
       
a=[]
b=int(input("enter the length of list"))
for j in range(0,b):
    c=int(input("enter the element for list"))
    a.append(c)     
d= [k for k in a if k >= 0]
  
print(d)
