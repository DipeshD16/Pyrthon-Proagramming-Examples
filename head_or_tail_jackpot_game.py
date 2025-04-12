import random
# This is a simple coin toss game where the user can bet on either heads or tails.
# The user starts with 100$ and can win or lose money based on their guesses.
# The goal is to reach a jackpot of 200$.
# The user can continue playing until they either win the jackpot or run out of money.
user_money = 100
jackpot = 200
possibilities = ['head', 'tail']
while user_money!=jackpot:
    if user_money ==0:
        print("You lost all the money.")
        break
   
    computer_choice = random.choice(possibilities)
   
    user_input = input("Enter head or tail").lower()
    if user_input == computer_choice:
        print("Correct!")
        user_money +=9
        print(f"You're total money becomes {user_money}$")
    else:
        print("Incorrect.")
        user_money -=10
        print(f"You have left with {user_money}$")
if user_money ==200:
    print("Congratulations you won the jackpot 200$.")
   