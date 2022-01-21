import math
while True:
    mode=input("Enter the operation to perform :")
    if(mode=="addition"):
        x=input("enter the first number :")
        y=input("enter the second number :")
        z=int(x)+int(y)
        print("the sum is :",z)
    if(mode=="subtraction"):
        x=input("enter the first number :")
        y=input("enter the second number :")
        z=int(x)-int(y)
        print("the difference is :",z)
    if(mode=="multiplication"):
        x=input("enter the first number :")
        y=input("enter the second number :")
        z=int(x)*int(y)
        print("the product is :",z)
    if(mode=="division"):
        x=input("enter the first number :")
        y=input("enter the second number :")
        z=int(x)/int(y)
        print("the division is :",z)