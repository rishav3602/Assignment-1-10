'''
7. Write a program that asks the user to enter a number. You should print out a message to the user, either “That number is divisible by either 3 or 5”, or “That number is not divisible by either 3 or 5”. Be sure to consider the data type of the input you are taking in from the user. Use a single if/else block to solve this problem.
'''
num = int(input("Enter the number u wanna check : "))
if (num/3 or num/5):
    print(f"{num}  is divisible by either 3 or 5")
else:
    print(f"{num}  is not divisible by either 3 or 5")
  