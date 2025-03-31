import time
from random import randint
num_list = []
lottery_num_list = []
points = 0
print("Welcome to the lottery game!")
print("You have 6 chances to guess the winning number.")
time.sleep(1)
for i in range(1, 6):
    num = int(input("Enter a number between 1 and 48:"))
    print(f"number {i} = {num}")
    lottery_num = randint(1, 48)

    num_list.append(num)
    lottery_num_list.append(lottery_num)

    if lottery_num_list == num_list:
        print("Congratulations! you gguessed the winning the number.")
        points += 1
    else:
        print("You guessed the wrong number.")
        print(f"The winning numbber is {lottery_num}")

if points == 5:
    print("You won the jackpot.")
elif points == 4:
    print("You won the second prize")
elif points == 3:
    print("You won the third prize.")
elif points == 2:
    print("You won the fourth prize")
elif points == 1:
    print("You won the fifth prize")
else:
    print("You didnt win any prize.")

print(f"You're total points are {points}")
cash_prize = points* 100
print(f"You're total cash prize is {cash_prize}$")