from math import pi
r = float(input ("Input the radius of the circle : "))
area = str(pi * r**2);
print ("The area of the circle with radius " + str(r) + " is: " + area)

a = input("Input the Filename: ")
b = a.split(".")
print ("The extension of the file is : " + repr(b[-1]))
