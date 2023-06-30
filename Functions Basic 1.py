from string import printable
from math import pi
from random import randint
def numrandom():
    n= eval(input("enter a number: "))
    generate = ""
    for i in range(n):
        if i == 0:
            generate = generate + str(randint(1,9))
        else:
            generate = generate + str(randint(0,9))
    new_generate = int(generate)
    print(new_generate)

numrandom()

input()

def first_diff(s,t):
    for i in range(len(s)):
        if len(s) != len(t):
            print("unequal length")
            break
        if s[i] == t[i]:
            continue
        else:
            return "Differ at index " + str(i) + ": "+"Unidentical"
    else:
        return str(-1) +": " +"identical"
first_diff("ward", "warden")
print("---------------------------------------")
first_diff("ward", "warn")

input()
def first_diff(m,n):
    smaller = min([len(m), len(n)])
    for i in range(smaller):
        if m[i] != n[i]:
             print(i)
             return
        elif m == n:
            print("-1")
            return

first_diff("strike","stroke")
input()



def matches(m, n):
    count = 0
    smaller = min([len(m), len(n)])
    for i in range(smaller):
        if m[i] == n[i]:
            count = count + 1
    return count
print(matches("python","path"))
print(matches("striker","stroke"))

print(min(["C", "T"]))
print(min([2, 5]))
input()


radius = eval(input("Enter a radius here: "))
area = lambda pi, radius: pi * radius ** 2
print("circle area is ", round(area(pi,radius),2))

input()

def number(x):
    x= str(x)
    print('-'.join(list(x)))
number(5000)

input()


ucase = lambda x: x.upper()
s= "python"
for i in range(len(s)):
    print(ucase(s[i]),end='')
print()
allcase = lambda s: s.upper()
print(allcase(s))

input()
str = lambda printable: printable.index("T")
print(str(printable))


input()

# annoynmous function
a = 50;
b= 4
z= lambda a,b: a+b
print(z(a,b))

input()
def sumIndices(s):
    indsum = s.index(s[0] + s.index(s[-2]))
    if indsum % 2 == 0:
        return True
    else:
        return False
print(sumIndices("java"))
input()

#write a program that accepts 3 class input and outputs a list
# containing all three

def factors(n):
    n= int(n)
    factors_list=[]
    for i in range(2, n+1):
        if n % i ==0:
            factors_list.append(i)
    return factors_list
print(factors(30))
print(factors(60))
print(factors('30'))
input()

list1=[]
for i in range(3):
    car=input("Enter a car: ")
    list1.append(car)
print(list1)
input()

cars =[]
x = 'Lexus'
y = 'aston martin'
z = 'Lexus again'
cars.append(x)
print(cars)
cars.append(y)
print(cars)
cars.append(z)
print(cars)

input()
def sum_digits(num):
    num = abs(num)
    numstr = str(num)
    numlist = list(numstr)
    print(numlist)
    numlist =[int(x) for x in numlist]  #list Comprehension
    print(numlist)
    return sum(numlist)
print(sum_digits(352))
input()


s = "A function"
print(len(s))
print(s.split())
print(list(s))
print(list(str(205)))

input()
t = 17385.2
print(round(t,-3))

input()

print(abs(-4.3))
print(round(3.336,2))
print(round(345.2,-1))
print(round(345.2,-2))
input()

def measure(weight,p):
    new_weight = weight
    p = p.lower()
    if p == "kg":
        new_weight = weight / 1000
        print(weight, "Gram is", round(new_weight,3), "kilogram")
    elif p == 'oz':
            new_weight = weight / 28.35
            print(weight, "Gram is", round(new_weight,3), "Ounce")
    elif p == 'lbs':
            new_weight = weight / 453.6
            print(weight, "Gram is", round(new_weight,3), "Pound")
    # else:
    #     print("Invalid, Please enter either kg or oz or lbs in lowercase ")
measure(3500,'kG')
measure(3500,'OZ')
measure(3500,'lBs')
measure(3500,'kfghj')
input()

# Task
def incrementX(x=4):
    for i in range(5):
        x = x+3
    print(x)
incrementX()
input()


# Task
def incrementX(x=4):
    x = x+3*5
    return x
print(incrementX(4))
input()


# Method 2
def incrementX(x=4):
    x = x+3
    return x
print(incrementX(4))
input()

# Method 5
def incrementX(x):
    return x + 3
print(incrementX(4))


input()
# Method 3
def incrementX():
    x =4
    return x + 3
input()
print(incrementX())


input()
def multiple_print(name, age=18):
    print("Your Name is : ", name)
    if age >= 18:
        print(str(age)+"?" + " You are eligible to join the club")
    else:
        print("Too young!")

myname= input("Enter name: ")+ " "

multiple_print(myname,12)
multiple_print(myname)

input()




# write a function program that given a variable X as equal 4,
# increment value of X by 3 and return the result

def assignment(n):
    x = n+3
    return x
print(assignment(10))

input()


def convert(t):
    return t * 9/5 + 32
print(convert(20))

print(convert(20)+5)
print(convert(20+5))
input()
def multiple_string(string,n):
    print(string * n)
    print()

multiple_string('hello ',5)
multiple_string("A ",10)

input()
def hello(n):
    print("hello! " * n)

hello(5)

hello(10)

def draw_rect():
    print("*" * 20)
    print("*", " " * 16, "*")
    print("*", " " * 16, "*")
    print("*" * 20)

draw_rect()


