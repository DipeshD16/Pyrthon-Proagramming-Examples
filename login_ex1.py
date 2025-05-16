#This script is for a simple login system
#It will ask for a username and password
#If the username and password are correct, it will print a welcome message
#If the username or password is incorrect, it will print an error message
login_details = {'Dipesh':'Pass@123',
                 'Adira':'Adira@123',
                  'Rani': 'Rani@123'
}

while True:
    user_input_1 = input("Please enter your username: ")
   
    if user_input_1 in login_details:
        user_input_2 = input("Please enter the password: ")
           
        if user_input_2 in login_details[user_input_1]:
            print("Welcome to your desktop.")
            break
        else:
            print("Invalid input, try again")
    else:
        print("Invalid input, try again")
