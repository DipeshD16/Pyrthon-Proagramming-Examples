import random
import time
import json
import os

# Dictionary for choices
choices = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors'}

# Game logic dictionary
winning_combinations = {
    ('r', 's'): "Rock crushes Scissors!",
    ('s', 'p'): "Scissors cut Paper!",
    ('p', 'r'): "Paper covers Rock!"
}

# JSON file to store game history
DATA_FILE = "game_results.json"

def load_game_data():
    """Load existing game data from JSON file."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return {}

def save_game_data(player_name, user_score, comp_score, total_rounds):
    """Save game results to JSON file."""
    data = load_game_data()

    if player_name not in data:
        data[player_name] = {"games_played": 0, "games_won": 0, "total_rounds": 0, "total_score": 0}

    data[player_name]["games_played"] += 1
    data[player_name]["total_rounds"] += total_rounds
    data[player_name]["total_score"] += user_score

    if user_score > comp_score:
        data[player_name]["games_won"] += 1

    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

def get_valid_input():
    """Ensure user inputs a valid choice."""
    while True:
        user_choice = input("Choose 'r' for Rock, 'p' for Paper, or 's' for Scissors: ").lower()
        if user_choice in choices:
            return user_choice
        print("Invalid choice! Please enter 'r', 'p', or 's'.")

def play():
    """Main function to play the game."""
    print("\n🎮 Welcome to Rock-Paper-Scissors! 🎮\n")

    # Get player name
    player_name = input("Enter your name: ").strip().title()
    print(f"\nHello, {player_name}! Let's begin the game.\n")

    user_input_1 = input("Would you like to play Rock-Paper-Scissors? (y/n): ").lower()

    if user_input_1 != 'y':
        print("Thank you for your time. Goodbye!")
        return

    # Ask how many rounds the user wants
    while True:
        try:
            total_rounds = int(input("Enter the number of rounds you want to play (min 1, max 10): "))
            if 1 <= total_rounds <= 10:
                break
            print("Please enter a number between 1 and 10.")
        except ValueError:
            print("Invalid input! Enter a valid number.")

    print("\nGet ready! The game starts now...\n")
    time.sleep(2)

    user_score = 0
    comp_score = 0

    for i in range(1, total_rounds + 1):
        print(f"\nRound {i}:")
        time.sleep(1)

        user_choice = get_valid_input()
        comp_choice = random.choice(['r', 'p', 's'])

        print(f"\n{player_name} chose: {choices[user_choice]}")
        print(f"Computer chose: {choices[comp_choice]}")

        if user_choice == comp_choice:
            print("It's a TIE!")
        elif (user_choice, comp_choice) in winning_combinations:
            print(f"You WIN! {winning_combinations[(user_choice, comp_choice)]}")
            user_score += 1
        else:
            print(f"Computer WINS! {winning_combinations.get((comp_choice, user_choice), '')}")
            comp_score += 1

    print("\nGame Over!")
    print(f"\nFinal Score: {player_name} {user_score} - {comp_score} Computer")

    if user_score > comp_score:
        print(f"🎉 Congratulations, {player_name}! You won the game! 🎉")
    elif user_score < comp_score:
        print("😞 Computer won the game. Better luck next time!")
    else:
        print("It's a tie!")

    # Save game data to JSON
    save_game_data(player_name, user_score, comp_score, total_rounds)

    print("\nGame data has been saved successfully! ✅")
    print(f"\nThank you for playing, {player_name}! See you next time! 👋")

play()