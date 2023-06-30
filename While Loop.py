newlang = ""
lang = "PYTHON"
i = 0
while i < 3:
    newlang = newlang + lang[i].replace(lang[i], "*")
    i = i + 1
print(newlang)
print(newlang + lang[3: ])
input()

# A user score is 64. Write a program that counts how many random numbers (between 4 and 10)
# must be deducted from the user's score before it becomes negative.
from random import randint
count = 0
score = 64
while score >= 0:
    score -= randint(4,10)
    count+= 1
print(count)
print(score)

input()
#2
list = []
score = eval(input("Enter Score: "))
while score >69:
    score = score - 1
    list.append(score)
    if score == 69:
        print(list)
        print("You are 1 mark away from the pass mark. Resit exam!")

input()


#1a
def func(number, string):
    i = 0
    new = ''
    while i < 8:
        new = new + number[i].replace(number[i], "*")
        i = i + 1

    print(new + number[-4:])

#1b
    num_list = []
    for c in number[-4:]:
        num_list.append(c)
    print(num_list)

#1c
    null = []
    for c in string.lower():
        if c in 'aeiou':
            null.append(c)
    print(null)

func('07018957357','Korode')
input()

username = input("Enter Username: ")
pwd = input("Enter Password: ").lower()
while pwd != 'toodope':
    username = input("Incorrect! Re-enter Username: ")
    pwd = input("Incorrect! Re-enter Password: ").lower()

print("Succesful! You are now logged in")

input()

while True:
    username = input("Enter Username: ")
    pwd = input("Enter Password: ")
    if pwd == 'toodope':
        print ("Succesful! You are now logged in")
        break
    else:
        print("Incorrect Passsword!")
input()


num = eval(input("Enter a number: "))
i = 2
while i <= num and num%i != 0:
    i += 1
if i == num:
    print("Prime")
else:
    print("Not Prime")
print(i)
input()


# Using a While loop only, print all even numbers between 0 and 50, excluiding 50
i = 0
while i <50:
    print (i)
    i += 2

input()

while True:
    state = input("Enter State: ").lower()
    if state == "lagos":
        print("Validity period for Lagos registeration has expired")
        break
    name = input('Enter Name: ')
    age = input("Enter Age: ")
    sex = input ("Enter Sex: ")

input()

# ----------------- NEVER ENDING LOOP ------------------------
#     - "While True" throws the user into a never ending loop
#        in a program.
#     - If statements are the only way to break out of an
#       infinite never ending loop

while True:
    temp = eval(input("Temperature in celsius: "))
    print("In Fahrenheit that is", round(9/5 * temp + 32, 1), "fahrenheits")
    if temp == -1000:
            print("Bye")
            break
input()

while True:
    temp = eval(input("Enter Temperature: "))
    if temp<=40:
        print("You are covid-19 patient")
        break
input()
# ------------------------------------------------------------
# ------------------- ASSIGNMENT -----------------------------
# A boy is 10 yrs of age and his father 4 times his age. Write a function
# that takes in both ages and determines(returns) in how many yrs the
# father will become 3 times his son's age.
def age(boy,dad):
    count = 0
    while dad/boy != 3:
        count += 1
        boy = boy + 1
        dad = dad + 1
    print("in", count, "yrs time,when the Boy will be",str(boy),"years, \nand the Dad will be",(dad),"years."
"The Dad will be 3 times\nthe boys age.")

age(10,10*4)
input()

# 2ND METHOD
def processAges(ageFth, ageSon):
    count = 0
    while True:
        ageFth += 1
        ageSon += 1
        count += 1
        if ageFth == ageSon*3:
            print("Will be 3 times son's age in", count, "yrs")
            break
processAges(10,40)
input()
# ---------------------------------------------------------------

age = eval(input("Enter Your Age: "))
while age > 17:
    print("You are an Adult")
    age = eval(input("Enter Your Age: "))
print("You are a minor")
input()

temp = 0
while temp < 40:
    temp = eval(input("Enter your body temperature: "))
print("You are a Covid-19 patient")
input()

temp = eval(input("Enter a Te   q   mperature in Celsius: "))
while temp < -273:
    temp = eval(input("Ogbeni! Enter a valid temperature: "))
print("In a Fahrenheit that is", round(9/5 * temp * 32,1),"Fahrenheit")
input()

#  ------------------ Differences between For Loop & While Loop ---------
# -- While Loop increment method
i = 0
while i < 10:
    print(i)
    i = i + 1
(input)

# -- For Loop Auto Increments
for i in range(10):
    print(i)
input()

from random import randint
randnum = randint(1,5)
x = 0
while x != randnum:
    x = eval(input("Guess the secret number: "))
print("Congratulations! You've guessed the right number")

input()

from random import randint
randnum = randint(1,9)
x = eval(input("Guess the random  number: "))
while x != randnum:
    x = eval(input("Wrong! Guess again: "))
print("Congratulations! You've guessed the right number")

input()

num = eval(input("Enter a number: "))
while num < 10:
    num = num - 1
    print(num)
    if num == -12:
        break

input()

# Request for a nbumber from the user and let the variable be num, while num is less than 10
num = eval(input("Enter a number: "))
while num<10:
    num = num - 1
    print(num)

input()

i = 0
while i < 10:
    print(i)

input()

a = 5
while a < 10:
    print("Hi")