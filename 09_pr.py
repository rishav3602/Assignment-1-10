'''
9. Take two variable radius_1 and radius_2 and calculate the area of circle_1 and circle_2. Also print which circle has large area. If area is equal then print area is equal.
'''
radius_1 = int(input("Enter the value of radius 1"))
radius_2 = int(input("Enter the value of radius 2"))
area_1 = 3.14*radius_1*radius_1
area_2 = 3.14*radius_2*radius_2
if (area_1>area_2):
    print("Circle is greater in area")
elif(area_1<area_2):
    print("Circle two is greater")
else:
    print("Both the circles have equal area")