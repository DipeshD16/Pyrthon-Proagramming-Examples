import time

print("Welcome to the Quiz")
answer = input("Would you like to play the guiz? ")
time.sleep(1)

if answer.lower() != "yes":
    print("Thank you for the interaction.")
    quit()

print("Get ready for the first question.")
time.sleep(2)
score = 0

answer = input("What is CPU stand for? ")
time.sleep(1)
if answer.lower() == "central processing unit":
    print("Correct answer!")
    score += 1
    time.sleep(1)
    print("Score updated.")
else:
    print("wrong answer.")

time.sleep(1)

answer = input("What is GPU stand for? ")

time.sleep(1)
if answer.lower() == "Graphical processing unit":
    print("Correct answer!")
    score += 1
    print("Score updated.")
else:
    print("wrong answer.")

time.sleep(1)

answer = input("What is RAM stand for? ")
time.sleep(1)
if answer.lower() == "random access memory":
    print("Correct answer!")
    score += 1
    print("Score updated.")
else:
    print("wrong answer.")

time.sleep(1)
answer = input("What is CPU stand for? ")
time.sleep(1)

if answer.lower() == "central processing unit":
    print("Correct answer!")
    score += 1
    print("Score updated.")
else:
    print("wrong answer.")

time.sleep(1)

answer = input("What is CPU stand for? ")
time.sleep(1)

if answer.lower() == "central processing unit":
    print("Correct answer!")
    score += 1
    print("Score updated.")
else:
    print("wrong answer.")

time.sleep(1)

print(f"total score is {score}")
time.sleep(1)

print("Thank you for playing the quiz. ")
time.sleep(1)

print("Good bye")