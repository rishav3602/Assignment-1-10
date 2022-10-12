'''
4. Take 3 variables and assign integer values to them. Find the largest variable, by only using the if and else conditions.
'''

a = int(input("Enter the value of a : "))
b = int(input("Enter the value of b : "))
c = int(input("Enter the value of c : "))
if (a>b):
    g = a
else:
    g = b
if (b>c):
    h = b
else:
    h = c

if g>h:
    print(f"The greatest of all the three number is {g}")
else:
    print(f"The greatest of all the three number is {h}")