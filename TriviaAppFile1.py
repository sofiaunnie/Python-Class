from random import randint
global ent_score
global sp_score
global lf_score

def optione():
    while True:
        opt = input(">>> ").upper()
        if opt == 'Y':
            return 'Y'
        elif opt == 'N':
            return 'N'
        else:
            print("Invalid input\nEnter yes[Y] or no[N]")
            continue


def check_answer(answer, guess):
    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG")
        return 0


def display_score(function):
    print(f"{'=' * 10}\nRESULT\n{'=' * 10}")

    print(f"Your answers: {', '.join(function[0])}")
    print(f"Correct answers: {', '.join(function[1])}")
    print(f"Your Score: {function[2]}")
    # if int(function) >= 3:
    #     print("You passed this round: ")
    # else:
    #     print("You lost this round!")


# Functions for each category
def ent_trivia():
    ent_score = 0
    entertainment = [
        ("Which of the actors in the TV series 'Community' also starred in the movies 'Vacation' and 'Fletch'?: ", "A"),
        ("Who starred in 'Bad Boys,' 'Independence Day,' 'Men in Black,' 'Enemy of the State' and 'Ali'?: ", "B"),
        ("What BBC program is presented by Jeremy Clarkson, Richard Hammond and James May?: ", "C"),
        ("What movie was marketed with the tagline: 'Who you gonna call?': ", "A"),
        ("Who plays Lucius Fox, chief executive officer of Wayne Enterprises and Bruce Wayne's armorer, in 'The Dark "
         "Knight'?: ", "C"),
        ("In which of these movies does Nicholas Cage's character not have any superpowers: ?: ", "A")
    ]

    ent_options = (["A. Chevy Chase", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerberg"],
                   ["A. Jason stathem", "B. Will Smith", "C. Silvester stallion", "D. Jet li"],
                   ["A. Lonely Island", "B.Monty Python", "C.Top Gear ", "D. SNL"],
                   ["A. Ghostbusters", "B. Spit in your Grave", "C. sometimes", "D. What's Earth?"],
                   ["A. Scott Adkins", "B.Will Smith", "C. Morgan Freeman", "D.Vin Diesel"],
                   ["A. Kick-Ass", "B. Next", "C.The Sorcerer's Apprentice", "D. Ghost Rider"])
    correct_answers = [i[1] for i in entertainment]
    guesses = []

    num = randint(1, 5)
    print(f"{'-' * 20} ENTERTAINMENT {'-' * 20}")
    print(entertainment[num][0])
    for i in ent_options[num]:
        print(i)

    b = True
    while b:
        guess = input("Enter (A,B,C OR D) : ").upper()
        if guess not in ['A', 'B', 'C', 'D']:
            continue
        else:
            print("Are you sure of your choice,\n[Y] for yes and [N] for No")
            hold_answer = optione()
            if hold_answer == 'Y':
                guesses.append(guess)
                ent_score += check_answer(correct_answers[num], guess)
            elif hold_answer == 'N':
                print(entertainment[num][0])
                for i in ent_options[num]:
                    print(i)
                    continue
            else:
                pass
        break
    return ent_score


def sport_trivia():
    sports = [("In which US state is the Masters golf played?: ", "A"),
              ("In which sport is Jordan Spieth famous?: ", "C"),
              ("Giants play baseball in which city?: ", "B"),
              ("Hash marks, hook and lateral, and line of scrimmage are terms from which sport?: ", "D"),
              ("Home run, pitcher, and base are terms used in which sport?: ", "A"),
              ("In which European country would you find the world's oldest golf club?: ", "C")
              ]

    sports_options = (["A. Georgia", "B. Germany", "C. Russia", "D. America"],
                      ["A. Baseball", "B. Long Tennis", "C. Golf", "D.Table Tennis"],
                      ["A. Italy", "B. San Francisco", "C. China", "D. Dubai"],
                      ["A. Basketball", "B. Rugby", "C. American Football", "D. Football"],
                      ["A. Baseball", "B. Long Tennis", "C. Golf", "D. Cricket"],
                      ["A. Finland", "B. Venezuela", "C. Scotland", "D. Spain"])

    correct_answers = [i[1] for i in sports]
    guesses = []
    sp_score = 0
    num = randint(1, 5)
    print(f"{'-' * 20} SPORTS {'-' * 20}")
    print(sports[num][0])
    for i in sports_options[num]:
        print(i)

    b = True
    while b:
        guess = input("Enter (A,B,C OR D) : ").upper()
        if guess not in ['A', 'B', 'C', 'D']:
            continue
        else:
            print("Are you sure of your choice,\n[Y] for yes and [N] for No")
            hold_answer = optione()
            if hold_answer == 'Y':
                guesses.append(guess)
                sp_score += check_answer(correct_answers[num], guess)
            elif hold_answer == 'N':
                print(sports[num][0])
                for i in sports_options[num]:
                    print(i)
                continue
            else:
                pass
        break
    return sp_score


def lifestyle_trivia():
    lifestyle = [
        ("Fried dough balls called struffoli are a Christmas favorite in which city?: ", "A.Naples"),
        (
        "Via San Gregorio Armeno, a street with many makers of traditional wooden nativity scenes, is in which city?: ",
        "C"),
        ("What pulse is said to represent wealth, and often eaten at New Year?: ", "B.Lentils"),
        ("What color of underwear is traditionally worn at New Year?: ", "D"),
        ("The tradition of eating seven fish dishes on Christmas Eve took hold in which other country after extensive "
         "Italian immigration?: ", "A"),
        ("Children in Sicily leave which items out for Santa Lucia to fill with presents?: ", "B")
    ]

    lifestyle_options = (["A. Naples", "B. Sydney", "C. America", "D. India"],
                         ["A. Canada", "B. Europe", "C. Naples", "D. Sydney"],
                         ["A. German", "B. Lentils", "C. China", "D. Germany"],
                         ["A. White", "B. Orange", "C. Purple", "D. Red"],
                         ["A. United States", "B. Mexico", "C. Spain", "D. Italy"],
                         ["A. Philippines", "B. United States", "C. Canada", "D. England"])
    correct_answers = [i[1] for i in lifestyle]
    guesses = []
    lf_score = 0
    num = randint(1, 5)
    print(f"{'-' * 20} SPORTS {'-' * 20}")
    print(lifestyle[num][0])
    for i in lifestyle_options[num]:
        print(i)

    b = True
    while b:
        guess = input("Enter (A,B,C OR D) : ").upper()
        if guess not in ['A', 'B', 'C', 'D']:
            continue
        else:
            print("Are you sure of your choice,\n[Y] for yes and [N] for No")
            hold_answer = optione()
            if hold_answer == 'Y':
                guesses.append(guess)
                lf_score += check_answer(correct_answers[num], guess)
            elif hold_answer == 'N':
                print(lifestyle[num][0])
                for i in lifestyle_options[num]:
                    print(i)
                continue
            else:
                pass
        break
    return lf_score





# Main Program
print('--------------------------Dune Entertainment--------------------------------------')

print("Welcome to the Maiden Trivia game")

while True:
    user_name = input(f"\n Enter your name: \t").title()
    if [i for i in user_name if not (i.isalpha() or i.isspace())]:
        print("Enter a valid name...")
    else:
        print("Welcome", user_name)
        break

print("It's Game Time..... \n"
      "Dune entertainments requires that prospective contestants complete some trivia/quizzes from different "
      "categories to qualify\n for maiden edition of their competition. ")

pick = {'1': 'ent', '2': 'sp', '3': 'lf'}
print("The Categories for this game are ")

print(f"1 Entertainment \n2 Sport \n3 Lifestyle")

category1 = (input("Pick Category: "))
while category1 not in pick.keys():

    print('invalid input! please enter a valid category')
    category1 = (input("Pick a valid category: "))

else:
    if category1 == '1':
        print("The Category you have chosen is Entertainment.")
        print(ent_trivia())
    elif category1 == '2':
        print("The Category you have chosen is Sports.")
        print(sport_trivia())
    elif category1 == '3':
        print("The Category you have chosen is Lifestyle")
        print(lifestyle_trivia())

while category1 == '1':
    pick23 = {'2': 'sp', '3': 'lf'}

    print("The Remaining Categories for this game are ")
    print(f"2 Sport \n3 Lifestyle")

    category2 = (input("Pick Category: "))

    while category2 not in pick23.keys():

        print('invalid input! please enter a valid category')
        category2 = (input("Pick a valid category: "))

    else:
        if category2 == '2':
            print(" ")
            print("The Category you have chosen is Sport ")
            print(" ")
            print(sport_trivia())

            print(" ")
            print("The last Category is Lifestyle")
            print(" ")
            print(lifestyle_trivia())

        elif category2 == '3':
            print(" ")
            print("The Category you have chosen is Lifestyle")
            print(" ")
            print(lifestyle_trivia())

            print(" ")
            print("The last Category is Sports")
            print(" ")
            print(sport_trivia())


while category1 == '2':
    pick13 = {'1': 'ent', '3': 'lf'}

    print("The Remaining Categories for this game are ")
    print(f"1 Entertainment \n3 Lifestyle")

    category3 = (input("Pick Category: "))
    while category3 not in pick13.keys():

        print('invalid input! please enter a valid category')
        category3 = (input("Pick a valid category: "))

    else:
        if category3 == '1':
            print(" ")
            print("The Category you have chosen is Entertainment'")
            print(" ")
            print(ent_trivia())

            print(" ")
            print("The last Category is Lifestyle")
            print(" ")
            print(lifestyle_trivia())

        elif category3 == '3':
            print(" ")
            print("The Category you have chosen is Lifestyle")
            print(" ")
            print(lifestyle_trivia())

            print(" ")
            print("The last Category is Entertainment")
            print(" ")
            print(ent_trivia())

while category1 == '3':
    pick12 = {'1': 'ent', '2': 'sp'}

    print("The remaining Categories for this game are ")
    print(f"1 Entertainment \n2 Sport")

    category4 = (input("Pick Category: "))
    while category4 not in pick12.keys():

        print('invalid input! please enter a valid category')
        category2 = (input("Pick a valid category: "))

    else:
        if category4 == '1':
            print(" ")
            print("The Category you have chosen is Entertainer")
            print(" ")
            print(ent_trivia())

            print(" ")
            print("The last Category is Sports")
            print(" ")
            print(sport_trivia())

        elif category4 == '2':
            print(" ")
            print("The Category you have chosen is Sport'")
            print(" ")
            print(sport_trivia())

            print(" ")
            print("The last Category is Entertainment")
            print(" ")
            print(ent_trivia())

total_score = lf_score + ent_score + sp_score
print(total_score)
#
# mydetails = open('MyDetails.txt', "a")
# mydetails.write(user_name + ' ')
# mydetails.write(display_score(ent_trivia()))
# mydetails.write(display_score(sport_trivia()))
# mydetails.write(display_score(lifestyle_trivia()))
# # mydetails.write(str(age))
# mydetails.close()
# mydetails.write(f"{user_name} {display_score()} ")
