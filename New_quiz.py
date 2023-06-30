from random import randint

print("Welcome to the Maiden Trivia game")

while True:
    user_name = input(f"\n Enter your name: \t").title()
    if [i for i in user_name if not (i.isalpha() or i.isspace())]:
        print("Enter a valid name...")
    else:
        print("Welcome", user_name)
        break

pick = {'1' : 'ent', '2' : 'sp', '3' : 'lf'}
print("The Categories for this game are ")

print(f"1 Entertainment \n2 Sport \n3 Lifestyle")

category = (input("Pick Category: "))
while category not in pick.keys():

    print('invalid input! please enter a valid category')

    category = (input("Pick a valid category: "))

else:
    if category == '1':
       print("The Category you have chosen is Entertainment.")
       print(''' "Which of the actors in the TV series 'Community' also starred in the movies 'Vacation' and 'Fletch'?: ": "A",
        "Who starred in 'Bad Boys,' 'Independence Day,' 'Men in Black,' 'Enemy of the State' and 'Ali'?: ": "B",
        "What BBC program is presented by Jeremy Clarkson, Richard Hammond and James May?: ": "C",
        "What movie was marketed with the tagline: 'Who you gonna call?': ": "A",
        "Who plays Lucius Fox, chief executive officer of Wayne Enterprises and Bruce Wayne's armorer, in 'The Dark Knight'?: ": "C",
        "In which of these movies does Nicholas Cage's character not have any superpowers: ?: ": "A" ''')

    print(''' 
        ent_options = (["A. Chevy Chase", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerberg"],
                ["A. Jason stathem", "B. Will Smith", "C. Silvester stallion", "D. Jet li"],
                  ["A. Lonely Island", "B.Monty Python", "C.Top Gear ", "D. SNL"],
                  ["A. Ghostbusters", "B. Spit in your Grave", "C. sometimes", "D. What's Earth?"],
                  ["A. Scott Adkins", "B.Will Smith", "C. Morgan Freeman", "D.Vin Diesel"],
                  ["A. Kick-Ass", "B. Next", "C.The Sorcerer's Apprentice", "D. Ghost Rider"])
        ''')
    if category == '2':
        print("The Category you have chosen is Sports.")
    if category == '3':
        print("The Category you have chosen is Lifestyle")

if category is '1':
    print(" ")

