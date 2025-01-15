#This is the first version of the calculator
#user will be asked for numbers input and to choose arithmatic operation
import sys  #to break the program incase wrong input

user_input_1 = (input("Enter the first number: "))
try:        #check the entered string is integer or not
    num1 = int(user_input_1)
    #print(f"The number you entered is: {num1}")
except ValueError:
    print("You did not enter a number.")
    sys.exit()      #it stops the program if the entered string is not integer.

#repeat the same for 2nd number
user_input_2 = (input("Enter the second number: "))
try:
    num2 = int(user_input_2)
    #print(f"The number you entered is {num2}")
except ValueError:
    print("You did not enter a number.")
    sys.exit()
    
#starts arithmatic operation
operation = input("Enter the mathmatic operation you would like to do:")
if operation == '+':
    total = num1 +  num2
    print(f"{num1} + {num2} = {total}")
elif operation == '-':
    total = num1 - num2
    print(f"{num1} - {num2} = {total}")
elif operation == '*':
    total = num1 * num2
    print(f"{num1} * {num2} = {total}")
elif operation == '/':
    total = num1 / num2
    print(f"{num1} / {num2} = {total:.2f}")
else:
    print("You choose the wrong operator.")
print("Thank you for the input")
print("This project is complete.")
print("Next version is in OOPS.")
