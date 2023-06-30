
while True:
    if category == "Entertainment":
        questions = dict(Entertainment_questions)
        options = Entertainment_options[:]
        break
    elif category == "Sports":
        questions = dict(Sports_questions)
        options = Sports_options[:]
        break
    elif category == "Travel":
        questions = dict(Travel_questions)
        options = Travel_options[:]
        break
    else:
        print("Category - Entertainment | Sports | Travel: ")
        break




Entertainment_questions = {
# question format
# "What player has made the most 3 pointers in their career?: ": "C",

}

Entertainment_options = [
    #option format
    #["A. Ray Allen", "B. Reggie Miller", "C. Stephen Curry", "D. Larry Bird"]
    ]
# -----------------------------------------------------------------------------------------------------------------------------------------
Sports_questions = {

}

Sports_options = []
# -----------------------------------------------------------------------------------------------------------------------------------------
Travel_questions = {

}

Travel_options = []












def new_game(questions, options):
    guesses = []
    correct_guesses = 0
    question_num = 6

    for key in questions:
        print("-------------------------------------------------")
        print(key)
        for i in options[question_num - 1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)


# -------------------------
def check_answer(answer, guess):
    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("INCORRECT!")
        return 0


# -------------------------------
def display_score(correct_quesses, guesses):
    print("-------------------------------------------------")
    print("RESULTS:")
    print("-------------------------------------------------")

    print("Answers: ")
    for i in questions:
        print(questions.get(i))
    print("")

    print("Guesses: ")
    for i in guesses:
        print(i)
    print("")

    score = int((correct_quesses / len(questions)) * 100)
    print("Your score is: " + str(score) + "%")

