import time 
import random
def quiz_game():
    print("Welcome to the quiz game.")
    time.sleep(1)

    answer = input("Would you like to plat the quiz game?(yes/no) ")
    if answer != "yes":
        print("Thank you for the interaction. Goodbye.")
        return
    
    print("Get ready for the first question.")
    time.sleep(2)

    questions = {
        "What does CPU stand for? " : "central1 processing unit",
        "What does GPU stand for? " : "graphical processing uuunit",
        "What does RAM stand for? " : "random access memory",
        "What does ROM stand for? " : "read only memory"
    }
    

    score = 0
    total_questions = len(questions)

    questions_list = list(questions.items())
    random.shuffle(questions_list)

    for question, correct_answer in questions_list:
        user_answer = input(question + " ").strip().lower()
        time.sleep(1)

        if user_answer == correct_answer:
            print("Correct answer.")
            score +=1
        else:
            print(f"Wrong answer, the correct answer is {correct_answer}")

        print(f"Current score: {score}/{total_questions}")

        time.sleep(1)
    
    #final score and performance evaluation.
    percentage = (score/total_questions) * 100
    print(f"the quiz is over. Your final score is {score}/{total_questions} ({percentage:.2f}%)")

    if percentage == 100:
        print("Excellant. you got everything correct.")

    elif percentage >= 75:
        print("Good job. You did well.")
    
    elif percentage >= 50:
        print("You did okay.")
    
    else:
        print("You need to practice more.")

    print("Thank you for playing the quiz game.")

quiz_game()