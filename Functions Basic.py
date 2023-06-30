# Write a function that takes an integer n and returns a random integer with exactly n digits.
from random import randint
def rand(n):
    new = ''
    for i in range(n):
        new = new + str(randint(1,9))
    print (new)

rand(5)
input()


# Using Lambda
from random import randint
n = eval(input("Enter a Number: "))
rand = lambda n,randint: str(randint(1,9))* n

print(rand( n,randint))
input()

#2
from random import randint
n = eval(input("Enter a number: "))
rand = lambda n,randint: randint(10**(n-1),(10**n)-1)

print(rand(n,randint))
input()



input()
def first_diff(s,t):
    for i in range(len(s)):
        if len(s) != len(t):
            print('Unequal Lengths! Input strings of a same lenght')
            break
        if s[i] == t[i]:
            continue
        else:
            return "Differ at index" +str(i)+": "+"Unidentical"
    else:
        return str(-1)+": "+"Identical"

first_diff("Ward", "Warden")
print('------------------------')
first_diff("Stroke","Stroke")
print('------------------------')
first_diff("Stroke","Strike")

input()

def first_diff(m,n):
    smaller = min([len(m), len(n)])
    for i in range(smaller):
        if m[i] != n[i]:
            print (i)
        elif m== n:
            print(-1)


first_diff("Strike", "Stroke")

input()

def countdown(n):
    for i in range(n, 0, -1):
        print(i)
    print("Take Off")

countdown(7)
input()




# --------------------------- ANONYMOUS FUNCTION -------------------------------------
# #  Using a lambda function, compute the area of circle with a radius defined by user
from math import pi
r = eval(input("Enter Radius: "))
z = lambda pi,r: pi*r**2
print(round(z(pi,r),2))

input()

# Write a function program that takes in a number greater than 5000 and returns
# same number with seperators which are hyphens

def fun(n):
    n = str(n)
    return "-".join(list(n))

print(fun(7500))
input()

#  We can change all letters of a string to uppercase characters one at a time
ucase = lambda x:x.upper()
s = "python"
for i in range(len(s)):
    print(ucase(s[i]), end = "")

#  Convert all the same time(not one character at a time)
allcase = lambda s:s.upper()
print(allcase(s))

input()

# Using lambda function, return the index of "T" in printable
from string import printable
t = printable
z = lambda t: t.index("t")
print(z(t))

input()
# Let's add tw0 numbers using Anonymous Function
a = 50
b = 4
z = lambda a,b: a+b
print(z(a,b))

input()


# Create a function that returns True if the sum of indices of first and second
# last chars of a string is even and false otherwise.

def sumIndices(s):
    indsum = s.index(s[0]) + s.index(s[-2])
    if indsum % 2 == 0:
        return True
    else:
        return False
print(sumIndices("Welcome"))
print(sumIndices("Java"))
print(sumIndices("Mysql"))

input()



def first_diff(m, n):
    count = 0
    larger = max([len(m), len(n)])
    for i in range (larger):
            if n[i] != m[i]:
                count-= 1
    return count


print(first_diff('python','path'))

input()



def matches(m, n):
    count = 0
    smaller = min([len(m), len(n)])
    for i in range (smaller):
            if m[i] == n[i]:
                count+= 1
    return count


print(matches('python','path'))

input()


def factors(n):
    n = int(n)
    factors_list = []
    for i in range(2, n+1):
        if n % i == 0:
            factors_list.append(i)
    return factors_list

print(factors(30))
print(factors(60))
print(factors("30"))
input()

# Write a program that accepts 3 car inputs and outputs a list containing all 3.
carlist = []
for i in range(3):
    cars = input("Enter a car brand: ")
    carlist.append(cars)
print(carlist)

input()


cars = []
x = "lexus"
y = "aston martin"
z = "Dodge Charger"
cars.append(x)
print(cars)
cars.append(y)
print(cars)
cars.append(z)
print(cars)

input()

#  Write a function called sum_digits that is given an integer num and then
#  returns the sum of the digit of num

# Method 1
def sum_digits(num):
    num = abs(num)
    numstr = str(num)
    numlist = list(numstr)
    numlist = [int(x) for x in numlist]
    print(numlist)
    return sum(numlist)
print(sum_digits(352))
print(sum_digits(304))
print(sum_digits(-304))

input()
# Method 2
def sum_digits(x):
    x = abs(x)
    x = list(str(x))
    x = int(int(x[0]) + int(x[1]) + int(x[2]))
    return x

print(sum_digits(352))
print(sum_digits(304))
print(sum_digits(-304))

input()

# BUilt-in String Functions
s = "A function"

print(len(s))
print(s.split())
print(list(str(205)))
input()

# User Defined Built In Functions
t = 17385.2
print(round(17385.2,-3))

input()
print(abs(-4.3))
print(round(3.336,2))
print(round(345.2,-1))
print(round(345.2,-2))

input()
# # METHOD 1
# def incrementX():
#     x = 4
#     for i in range(5):
#         x = x+3
#     return x
# print(incrementX())
# input()
#
# # METHOD 2
# def incrementX(x):
#     return x + (3*5)
# print(incrementX(4))
# input()
#
# # METHOD 3
# def incrementX():
#     x = 4
#     return x+3
#
# print(incrementX())
#
# input()
#
# def multiple_print(name,age=18):
#     print("Your name is: ", name)
#     if age >= 18:
#         print(str(age)+"!"+"You are eligible to join the club")
#     else:
#         print("Too Young")
# myname = input("Enter your name: ")
# multiple_print(myname,12)
# multiple_print(myname)
#
# input()
#
# def multiple_print(string,n):
#     print(string*n)
#     print()
# myname = input("Enter name: ") + " "
# myage = eval(input("Enter age: "))
#
# multiple_print(myname,myage)
#
# input()
#
# # Write a function that accepts value in grams and converts it to kilograms, ounces and pounds if a
# # if a string p is "kg", "oz" or "lbs"

# def convert(gram, str):
#     str = str.lower()
#     if str == 'kg':
#         print("There are",gram,"grams in ", gram/1000,"Kilograms")
#     elif str == 'oz':
#         print("There are", gram, "grams in ", round((gram/28.34952),3), "ounces")
#     elif str == 'lbs':
#         print("There are", gram, "grams in ", gram*0.0022, "Pound")
#     else:
#         print("You have passed Incorrect parameters, enter one of  'kg', 'oz', 'lbs'")
#
# convert(3500,'LBS')
# convert(3500,'kg')
# convert(3500,'oz')
#
input()


# Using a function that accepts 2 arguements, draw a trapezium of stars
def trampezium(n,s):
    for i in range(n,s):
        print("*"*i)

trampezium(3,8)

input()
# Write a function that accepts 3 different arguements: name, age and occupation and outputs:
# a. user's sector/industry between Real estate,ICT and Hospitality
# b. The age of the user in 5 years time

def processUser(name,age,occupation):
    if occupation == "Agent":
        print("You are in the Real Estate sector")
        print("In 5years: ", age + 5)
    elif occupation == "Chef":
        print("You are in the Hospitality sector")
        print("In 5years: ", age +5)
    elif occupation == "Web Designer":
        print("You are in the ICT sector")
        print("In 5years: ", age + 5)
    else:
        print("Designated Occupation unknown")

processUser('David',22,'Agent')
print('-------------------------------')

processUser('Jeff',34,'Web Designer')
print('-------------------------------')

processUser('Flora',26,'Chef')
print('-------------------------------')

input()

# Write a function program that given a variable x=4, increment the value of x by 3 and returns the result.
# Method 1
def incrementX():
    x = 4
    return x+3
print(incrementX())

input()

# Method 2
def incrementX(x):
    return x+3
print(incrementX(4))

input()

def convert(t):
    return t*9/5+32

print(convert(20)+5)
print(convert(20+5))

input()

def multiple_string(string, n):
    print(string *n)
    print()

multiple_string("Hello ",5)
multiple_string("A",10)

input()

def hello(n):
    print("Hello "*n)

hello(5)


input()

def draw_rect():
    print("*"*20)
    print("*"," "*16,"*")
    print("*", " " * 16,"*")
    print("*" * 20)

draw_rect()

input()

def hello():
    print("Hello!")

hello()