#3. Use if else condition to verify that dataype of `input()` method in python is always string.

a = input("Enter the value of a : ")
if (type(a) == int or bool or float) :
    print("It is not a string")
else:
    print("It is a string")