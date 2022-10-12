'''
10. Check whether a year is leap year or not. Use nested if...else to solve this problem. A leap year is exactly divisible by 4 except for century years (years ending with 00). The century year is a leap year only if it is perfectly divisible by 400.
'''

year = int(input("Enter the year you wanna check : "))
if (year%4==0):
    if(year%100 != 0):
        print("Given year is a leap year")
    elif(year%400==0):
        print("Given year is leap year")
    else:
        print("Given year is not a leap year")
else:
    print("Given is a not a leap year")
