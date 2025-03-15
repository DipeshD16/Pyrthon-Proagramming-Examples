import time, random

choices = {"r": "rock", "p": "paper", "s":"scissor"}
winning_combinations = {}
def get_valid_input():
    '''Ensures user only enters "r", "p" or "s".'''
    while True:

        user_input = input("Please enter you choice, 'r' for rock, 'p' for paper or 's' for scissor: ").lower()
        if user_input in choices:
            return user_input
        else:
            print("Invaid input. Please enter 'r', 'p', or 's'.")

def play():
    '''main game function. '''
    print("Welcome to the Rock-Paper-Scissor game.")

    while True:
        user_input_1 = input("Would you like to play the game (y/n): ").lower()
        if user_input_1 == 'n':
            print("Thank you for your interaction, Goodbye!")
            return
        elif user_input_1 == 'y':
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

    print("Best of five rounds. First three to win the game.")
    time.sleep(1)
    user_score, comp_score = 0, 0

    for round_num in range(1, 6):
        print(f"\nRound {round_num}: ")
        time.sleep(1)

        user_input = get_valid_input()
        comp_input = random.choice(['r', 'p', 's'])
        print(f"You choice: {choices[user_input]} Vs Computer choice: {choices[comp_input]}")

        if user_input == comp_input:
            print("Its a tie.")
        
        elif (user_input, comp_input) in winning_combinations:
            print("Congratulations! you won this round.")
            user_score += 1
        else:
            print("Computer won this round.")
            comp_score +=1
        if user_score ==3 or comp_score == 3:
            break


    print("\nFinal Score:")
    print(f"\nUser score: {user_score}/5")
    print(f"\n Computer score: {comp_score}/5")

    if user_score > comp_score: 
        print("You won the game.")
    elif user_score < comp_score:
        print("Computer won the game.")

    else:
        print("Its a tie.")

play()



        
