patient_temp = eval(input("Please enter temperature: "))
while patient_temp <= 40:
    print('You are a covid-19 patient')
input()



usertemp = eval(input("Please enter temperature in celsius: "))
while usertemp < -273:
    usertemp = eval(input("Invalid! Please enter a valid temperature: "))
print("In Fahrenheit that is:",round(9/5* usertemp + 32,1),"fahreinheits")
input()
#---FOR vs WHILE-----
#Using WHILE Loop
i = 0
while i < 10:
    print(i)
    i = i + 1
input()

#Using FOR Loop
for i in range(10):
    print(i)

input()

temp = 0
while temp != -1000:
  temp = eval(input('Enter a temperature(-1000 to quit) :'))
  print('In Fahrenheit that is,',9/5*temp+32)
  print('You are mad!')

input()
#Method 1
from random import randint
secret_num = randint(1,5)
guess = 0
while guess != secret_num:
    guess = eval(input('Guess the secret number:'))
print('You finally got it!')
input()

#Method 2
from random import randint
rand_num = randint(1,10)
userguess = eval(input('Guess the number:'))
print(rand_num)
while userguess != rand_num:
    userguess = eval(input('Invalid! Guess again:'))
else:
    print('You finally got it!')
input()
num = eval(input('Enter a number:'))
while num < 10:
    num = num - 1
    print(num)
    if num == -12:
        break
input()

i = 0
while i <10:
    print(i)
input()

a = 5
while a < 10:
    print("Hi")
