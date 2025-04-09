user_score = []
# This program will ask the user to enter their score in each subject.
# The program will stop asking for scores when the user enters a negative number.
# Finally, it will print the number of subjects in which the user got an A* (90 or above)
while True:
    user_input=  eval(input("Enter the score or (enter a negative number to stop): "))
    if user_input > 0:
        user_score.append(user_input)
    else:
        break
print(user_score)
count = 0
for i in range(len(user_score)):
    if user_score[i] >=90:
        count +=1
print("You got A* in", count, "subject.")
print(f"The avg score is {sum(user_score)/len(user_score):.2f}.")