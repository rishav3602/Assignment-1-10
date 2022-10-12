'''
8. Take user input for length and width. Then calculate the area of rectangle. Also print as per length and width whether its a square of rectangle.
'''
len = int(input("Enter the length of rectangle : "))
wid = int(input("Enter the width of rectangle : "))
area = len*wid
print(area)
if len == wid:
    print("This is a square")
else:
    print("This is a rectangle")
