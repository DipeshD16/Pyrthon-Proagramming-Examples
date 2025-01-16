#this is a program for the basic calculator
#It prompts the user for the kind of operation you want to do and proceeds
#It the user chooses division and the the second number is zero then the program gives error message
#if the user enters the wrong value for the numbers then  it prompts the user with an error message.

#define calculator as a class
class calculator:
        #defining the method
    def __init__(self):
        print("Basic calculator initialized.")
       
    def add(self, a, b):
        return a+b
    def subtract(self, a, b):
        return a-b
    def divide(self, a, b):
        if b==0:
            return "Error! Division by zero."
        return a/b
    def multiply(self, a, b):
        return a*b

calc = calculator()

#options for the user
while True:
    print("\nOptions")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiplication")
    print("4.Division")
    print("5.Exit")
   
    choice = input("Select an operation (1-5): ")
   
    if choice == '5':
        print("Exiting calculator! Thank you.")
        break
   
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    #valuerror for the incorrect input
    except ValueError:
        print("Invalid input! Please enter numeric values. ")
        continue
    #for the correct option
    if choice =='1':
        print(f"result: ", calc.add(num1. num2))
    elif choice == '2':
        print(f"result: ", calc.subtract(num1, num2))
    elif choice == '3':
        print(f"result: ", calc.multiply(num1, num2))
    elif choice == '4':
        print(f"result: ", calc.divide(num1, num2))
       
    else:
        print("Invalid input! Please select the correct input. ")
       