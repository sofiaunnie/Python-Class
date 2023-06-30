#Generate a random MTN Phone number that begins 070
from random import randint
print('070'+str(randint(10000000,99999999)))
input()
#Generate a random MTN Phone number that begins 070
from random import randint
num = '070'+str(randint(10000000,99999999))
print (num)
input()
from random import randint
num = str('070')
for i in range(8):
    num = num + str(randint(1,9))
print (num)

input()

from random import randint
score = 1000
for i in range(5):
    x = randint(5,100)
    print (x)
    score = score - x
print('Score is', score)

input()



#Write a program that computes the sum of five randum numbers generated.
#Display all 5 numbers and their sum.
from random import randint
sum = 0
for i in range (5):
    x = randint(5, 100)
    print (x)
    sum += x
print ("The Sum is ",sum )


input()
#Generate an ATM pin for a user, request that the user enter the correct pin after it has been generated
# if pin (input) entered by the user is wrong, display a message to that effect, otherwise allow them access
#With a message to that effect
from random import randint
pwd = randint(0,9)
for i in range (3):
    pwd = str(pwd) + str(randint(0,9))
print ('Your pin is',pwd)
for i in range(3):
    user = (input('Enter your Pin: '))
    if user != pwd:
        print("Please enter the correct pin")
    elif user == pwd:
        print('Welcome User!')
        break
    else:
        print ("Please contact your bank")



input()
#Write some code that joins a user's name with a 2 digit random number
from random import randint
username = input('Enter your Username: ')
x = randint(10,99)
print(username+str(x))
input()


print(str(7)+'Up')

input()
#Write a program that generates a random  decimal number between
# 1 and 10 with 2 decimal places of accuracy. E.g 1.23, 1.45, 7.32, 5.02 etc.
from random import randint
x = str(randint(1,10))+"."+str(randint(0,9))+str(randint(0,9))
decimal = float(x)
print(decimal)
print(decimal * 10)

input()


#Write a program that generates a random  decimal number between
# 1 and 10 with 2 decimal places of accuracy. E.g 1.23, 1.45, 7.32, 5.02 etc.
from random import uniform
x =  (round(uniform (1,10), 2))
print (x)

input()


# Write a program that generates and prints 50 random numbers between 3 and 6
from random import randint
for i in range (50):
    x = randint(3,6)
    print (x)

input()



# Write a program that generates a random number x, between 1
# and 50, a random number y betweeen 2 and 5 and computes x raised
# to the power of y.
from random import randint
x = randint (1,50)
y = randint (2,5)
print (x**y)

input()

# Write a program that joins a user's name with any 4-digit random number
from random import randint
username = input('Enter Username: ')
rand = randint (1000,9999)
print ( username+str(rand))

input()


# Write a program that generates 1000 random numbers between 1 and 100 and counts how many of them are multiples of 4
from random import randint
count = 0
for i in range (1,1000):
    randnum = randint(1,100)
    if randnum%4 == 0:
        count = count + 1
print (count)

input()




# Write a program that generate 7 random numbers between 1 and 10 and count how many are even
from random import randint
count = 0
for i in range (7):
    randnum = randint(1,100)
    if randnum% 2 == 0:
       count = count + 1
print (count)

input()

# WRITE A PROGRAM THAT GENERATES 10 RANDOM NUMBERS (BTW 1 AND 100)
# AND OUTPUTS THOSE GREATER THAN 25.
from random import randint
for i in range (10):
    rand = randint(1, 100)
    if rand > 25:
        print (rand)

input()

# All even numbers betweeen 1 and 23
for i in range (1,24):
    if i % 2 ==0 :
        print (i)

input()


# Write a simple program that outputs all even  numbers between 1 and 5
for i in range (1,6):
    if i % 2 == 0:
        print (i)
input()



from random import randint
score = 100
rand_num = randint(1,15)
for i in range(5):
    userguess = eval(input('Guess the number: '))
    if userguess == rand_num:
        score = score + 100
        print('New Score: ', score)
        break
    else:
        score = score - 1
        print ('New score: ', score)
print('Your finals score was: ', score)
print('random number was: ', rand_num)

input()

# METHOD 2
from random import randint
x = randint(5,25)
print (x)
for i in range (x):
    print("Hello ")
input()


from random import randint
# METHOD 1
x = randint(5,25)
print (x)
print ('Hello ' * x)

input()

from random import randint
x = randint(1,10)
print ('A random number between 1 and 10: ', x)