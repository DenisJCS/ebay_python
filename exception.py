# This code doesn't handle any exception
a = input("Enter number:")
b = input("Enter number:")
a = int(a)
b = int(b)
print (a / b)

#This one does handle division by 0

a = input("enter number:")
b = input("enter one more number:")
a = int(a)
b = int(b)
print(a / b)
try:
    print(a / b)
except ZeroDivisionError:
    print("Input error")


#This handle both 0 and incorrect input
try:
    a = input("enter number:")
    b = input("enter one more number:")
    a = int(a)
    b = int(b)
    print(a / b)
except (ZeroDivisionError, ValueError):
    print("Input error")


