from random import randint

score = eval(input("Enter a score: "))
lowered_scores=[]
while score >= 70:
    score -= 1
    lowered_scores.append(score)
    if score == 69:
        print("You are one score away")
print(lowered_scores)


input()

lang = "PYTHON"
i=0
new_lang = ''
while i < 3:
    aster = lang[i].replace(lang[i], '*')
    new_lang = new_lang +aster
    i = i + 1
print(new_lang + lang[3:])

input()


score = 64
countrand = 0
while score >= 0:
    rand = randint(4, 10)
    score -= rand
    countrand += 1
print(countrand)
print(score)





input()


input()
def ageGuess():
    boy =10
    father = boy * 4
    years = 0
    while (boy * 3) != father: 
        years += 1
        father += 1
        boy += 1
    print("father will be 3 times is son age in" , years , "years")

ageGuess()
input()

age = eval(input("Enter a number: "))

while age >17:
    age = eval(input("Enter a number: "))
print("You are a minor")
input()

patient = eval(input("Enter a temperature: "))
while patient <41:
    print("You dont have covid")
    patient = eval(input("Enter a temperature: "))
print("You are a covid patient")

input()

usertemp = eval(input("Please enter temperature in celsius: "))
while usertemp < -273:
    usertemp = eval(input("Invalid! Please enter a valid temperature:"))
print("In Fehrenheit that is: ", round(9/5 * usertemp + 32,1), "Fehrenheit")

input()
i = 0
while i<10:
    print(i)
    i=i+1
input()

for i in range(10):
    print(i)

input()
secret_num = randint(1,5)
guess = 0
while guess != secret_num:
    guess = eval(input("Guess the secret number: "))
print("you finally got it!")

input()

randnum = randint(1,10)
userguess = eval(input("Guess the random number: "))
print(randnum)
while userguess != randnum:
    userguess =eval(input("Guess the random number: "))
print("you got it right")
input()



num = eval(input("Enter a number: "))
while num < 10:
    num =num -1
    print(num)
    if num == -12:
        break

input()
i=0
while i<10:
    print(i)

input()

a = 5
while a < 10:
    print("Hi")