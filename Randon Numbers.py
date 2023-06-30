

input()
from random import randint, uniform

username = input("Please enter your Username: ")
password = input("Please enter your Password: ")
print(f'{username}, your password {"*" * len(password)} is {len(password)} letters long')

input()

birth_year = input('What\'s year were you born? ')

print('your age is', 2022 - int(birth_year))

input()



print("0.1%10 =", 0.1%10)

#generate a random mtn number dat begins with 070

pref= "070"
number= randint(10000000,99999999)
print(pref+str(number))

input()

#write a program that computes the sum of 5 random numbers generated
#display all 5 numbers and their sum

score=1000
for i in range(5):
    randnum = randint(5, 100)
    print(randnum)
    score = score - randnum

print("final score",score)

input()





###############################
num1 = randint(5,100)
num2 = randint(5,100)
num3 = randint(5,100)
num4 = randint(5,100)
num5 = randint(5,100)
print(num1, num2, num3, num4, num5)
print(num1+num2+num3+num4+num5)

input()



# #write some codes that concatinate or join the user's name with a two digit random num
user= input("Enter your name: ")
x=randint(10,99)
print(user+ str(x))
input()

#generate an atm pin for a user
#request that the user enter the correct pin after it has been generated
#if pin input by the user is wrong display a message to that event
#other wise other them access

pin = str(randint(0,9))
for i in range (3):
    pin = str(pin) + str(randint(0,9))
balance= randint(0,99999)
print(pin)
userpin=(input("Enter your Pin: "))


if pin != userpin:
    print("incorrect Pin")
else:
    print("welcome your balance is", balance)


input()









input()
x= str(randint(1,10))+ "."+ str(randint(0,9))+ str(randint(0,9))
decimal=float(x)
print(decimal)
print(type(decimal))
print(decimal * 10)

print(str(7) + "up")

x=randint(1,50)
y=randint(2,5)
print('X random number is', x)
print('Y random number is', y)
power=x**y
print(x,'raise to power', y, 'is', power)

input()


for i in range(50):
    num = randint(3,6)
    print(num)

input()
input()

num1=uniform(1,10)
print(round(num1,2))

input()


input()
input()

count = 0
for i in range(1000):
    x = randint(1,100)
    if x % 4 == 0:
        count = count + 1
print(count)
input()

name=input('Enter your name ')
x = randint(0,9)
print (name,x,sep='')

input()

count = 0
for i in range(7):
    x = randint(1,10)
    if x % 2 ==0 :
        count = count + 1
print(count)
input()


for i in range(10):
    x = randint(1, 10)
    if  x > 25:
        print(x)

input()

for i in range(1,24):
    if i % 2 == 0:
        print(i)
input()



score=100
rand_num=randint(1,6)
for i in range(5):
    userguess = eval(input("Guess the number: "))
    if userguess == rand_num:
        score = score + 10
        print("New score: ",score)
        break
    else:
        score =score - 1
        print("New score: ",score)
print("Your final score was: ",score)
print("Random number was: ",rand_num)

input()

x=randint(5,25)
print(x)
for i in range (x):
    print('hello')
input()

x = randint(5,25)
print('Hello' * x)
input()

x = randint(1,10)
print('A random number between 1 and 10:', x)

