import random, time

def play():
    user_input_1 = input("Would you like to play rock paper scissor, press 'y' for yes and 'n' for no: ")
    user_input_1 = user_input_1.lower()
   
    if user_input_1 == 'n':
        print("Thank you for interaction.")
        quit()
   
    print("We will have total 5 rounds and whomsoever wins the maximum rounds will be the winner.")
    time.sleep(2)
    print("Get ready.")
    time.sleep(2)
    user_score = 0
    comp_score = 0
    for i in range(1,6):
        print(f"round {i}: ")
        time.sleep(2)
        user_input = input("Please select your choice: press 'r' for rock, 'p' for paper or 's' for scissor: ")
        comp = random.choice(['r', 'p', 'c'])
       
        if user_input == 'r' and comp == 'r':
            print("its a TIE")
       
        elif user_input == 'r' and comp == 'p':
            print("Computer won.")
            comp_score +=1
       
        elif user_input == 'r' and comp == 's':
            print("Congratualtions! you won. ")
            user_score +=1
       
        elif user_input == 'p' and comp == 'r':
            print("Congratulations! you won")
            user_score +=1
           
        elif user_input == 'p' and comp == 'p':
            print("its a TIE")
       
        elif user_input == 'p' and comp == 's':
            print("Computer won.")
            comp_score +=1
       
        elif user_input == 's' and comp == 'r':
            print("Computer won.")
            comp_score +=1
       
        elif user_input == 's' and comp == 'p':
            print("Congratulations! you won. ")
            user_score +=1
           
        else:
            print("its a TIE")
   
    if user_score > comp_score:
        print("User won")
   
    elif user_score < comp_score:
        print("Computer won")
       
    else:
        print("its a TIE")
   
    print(f"User Score = {user_score}/5")
    print(f"Computer Score = {comp_score}/5")
           
       
           
           

play()