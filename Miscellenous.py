#STATISTICS
import statistics
data = [9,74,4,3,3.25,2,6,1.25,8]
data.sort()
print(data)
meandata = statistics.mean(data)
mediandata = statistics.median(data)  #Middle Number after sorting
variancedata = statistics.variance(data)  #variance
sd = statistics.stdev(data)               #Standard Deviation
print(meandata, " : ", round(meandata,1))
print(mediandata, " : ", round(mediandata,1))
print(variancedata, " : ", round(variancedata,1))
print(sd, " : ", round(sd,1))

input()
#DICTIONARY CHANGES
names = {'temi':30, 'godwin':45, 'charles':36}
names.update({'martinez':40, 'sinclair':35 })
#print(names)

        #OR
#names['martinez'] = 40
#print(names)
#
print(names.get('godwin'))
print(names['godwin'])

input()

#LIST CHANGES
books = ['primary','secondary','motivational','professional','religious']
#books.pop(3)
#print(books)

#b = books.pop(1)
#print(b)

for i in range(5):
    books.pop()
print(books)

input()

#TASK
actor = "Vin Diesel"
movie = "Chronicles of Riddick"
money = "700 pounds"

print("My favorite actor is \"{}\" and the best movie he has done so far is \"{}\". Hopefully"
      " the movie pulls in 700 pounds on its box office premiere ".format(actor,movie))
input()

#IN OPERATOR/STRING METHODS
print('A' in 'Apple') #Returns boolean True
letter = "a"
word = "Apple"
print(letter in word) #Returns boolean False
print(letter in word.lower()) #Returns boolean  )


#FORMATTING AND PLACEHOLDERS
snack = "burger"
drink = "Coca-Cola"
drink2 = "juice"

print(f"I drink only {drink2}")    #FORMATTED STRING
print("He said \"let us go\"")
print("Pius said, my favorite drink is \"{}\".He also said his favourite snack is \"{}\""
      .format(drink2,snack))  #PLACEHOLDERS
print('------------------------------------------------------------------------------------')
#task 1
print(f"Pius said, my favorite drink is \"{drink.upper()}\". He also said his favourite snack is "
      f"\"{snack.upper()}\"")
input()

input()

#AUTOMATION
import pyautogui as pgi
import time

# -----------AUTOMATE KEY COMBINATION (HOTKEYS) ----------
pgi.hotkey(['Ctrl' + 'C'])

#SAMPLE AUTOMATE TASK
#collect user inut or a youtube video and search for it

#using snipping tool method
usersearch = input("What video are you searching for:")
min_btn = pgi.locateOnScreen("minimize.PNG")
pgi.click(min_btn)
time.sleep(3)
ntab = pgi.locateOnScreen("new_tab.PnG")
pgi.click(ntab)
pgi.click(264,77)
pgi.typewrite('www.youtube.com')
pgi.typewrite(['Enter'])
time.sleep(7)
s = pgi.locateOnScreen("search.PNG")
pgi.click(s)
pgi.typewrite(usersearch)
pgi.typewrite(['Enter'])
input()

#------using position method ----------- vv
usersearch = input("What video are you searching for:")
min_btn = pgi.locateOnScreen("minimize.PNG")
pgi.click(min_btn)
time.sleep(3)
ntab = pgi.locateOnScreen("new_tab.PnG")
pgi.click(ntab)
pgi.click(264,77)
pgi.typewrite('www.youtube.com')
pgi.typewrite(['Enter'])
time.sleep(7)
pgi.click(502,146)
pgi.typewrite(usersearch)
pgi.typewrite(['Enter'])

input()

#Initiate a new chrome tab(4 secnds later) and search for how to make egg rolls
#method 2
ntab = pgi.locateOnScreen("new_tab.PnG")
pgi.click(ntab)
pgi.moveTo(264,77)
pgi.click()
pgi.typewrite('How to make an egg roll')
pgi.typewrite(['Enter'])

input()
min_btn = pgi.locateOnScreen("minimize.PNG")
pgi.click(min_btn)
time.sleep(4)
pgi.click(402,28)
pgi.typewrite('How to make an egg roll')
pgi.typewrite(['Enter'])

input()
# ----------CLICK AND SEARCH CHROME ---------
min_btn = pgi.locateOnScreen("minimize.PNG")
pgi.click(min_btn)
time.sleep(3)
pgi.click(264,77)

#-------AUTOMATE KEYBOARD TYPING--------------
pgi.typewrite('How to make a milkshake')

#------AUTOMATE ENTER KEYSTROKE -----------
pgi.typewrite(['Enter'])
input()
#task minimizing a window
#method 2
#1 locate minimize button on screen and save image
#2 use locateonscreen method

min_btn = pgi.locateOnScreen("minimize.PNG")
pgi.click(min_btn)

input()
#method 1
#1 find mouse position
#2 click on that position
#print(pgi.position())
# pgi.click(1159,16)

# PIXELS
# print(pgi.position())
input()
# ------------AUTOMATE A MOUSE RIGHT-CLICK ----------
pgi.rightClick()
input()

#CLOSING APPLICATIONS
import os
os.system('taskkill /f /im excel.exe')

input()
#OPENING APPLICATIONS

import os
os.chdir('C:\\Program Files\\Microsoft Office\\Office16')  #python recognizes forward slashes
os.system('excel.exe')

input()

#CHOICE FROM RANDOM
from random import choice
fruits = ['apple','cucumber','carrots','pomegrantes','strawberries']
chosen = choice(fruits)
print(chosen)

questions = "12345"
x = choice(questions)
print(x)

input()

#EXCEPTIONS
"""
Exceptions syntax
try:
code.........
except
code.......
else:
code........
finally: 
code.........
"""
try:
    #n = 12/0
    length = int(input("Enter a length: "))
    breadth = int(input("Enter a breadth: "))  #Entering string here raises valueError
    #breadth = input("Enter a breadth: ")   #Incorrect raises typeError
    sidesum = length + breadth              #Correct
    #sidesum = length + str(breadth)        #Incorrect raises typeError
except ValueError:
    print("Wrong Value!. Enter an Integer")
except ZeroDivisionError as ze:
    print("Error! You tried dividing by zero")
    print(ze)
#A type error occurs when you try to merge 2 incompatible data types e.g int and string
except TypeError:
    print("Cannot combine incompatible data types ")
else:
    perimeter = sidesum * 2
    print("The perimeter is {} ". format(perimeter))
#the finally block gets executed whether there is an error or not
finally:
    print("The user has entered in some input")  #Runs regardless

input()
#REMOVE WHITESPACE
too_much_space = "   hello          "
#print hello and the the length of hello + the number of white spaces
print(too_much_space, len(too_much_space))
#brings out hello and the length of hello
print(too_much_space.strip(),len(too_much_space.strip()))
#print hello and the the length of hello + the number of white spaces on the left
print(too_much_space.rstrip(),len(too_much_space.rstrip()))

input()

#DATE AND TIME
#dt is an allias i.e a temporary name
from datetime import datetime as dt
print(dt.now())

input()

from datetime import datetime
print(datetime.now())  #Returns current date and time
print(type(datetime.now()))

input()

from datetime import datetime
import time

d = datetime.now()
time.sleep(15)
m = datetime.now()
print(m.second - d.second)

input()

from datetime import datetime
d = datetime.now().month #Returns current month
print(d)

input()

from datetime import datetime
d = datetime.now().minute #Returns current minute
print(d)

input()

from datetime import datetime
d = datetime.now().year #Returns current year
print(d)

input()

import string
print(string.printable)
print('-----------------------------------')
print(string.punctuation)
print('-----------------------------------')
print(string.digits)

input()

import pyautogui as pgi
# import subprocess

import time

print("Hello")
time.sleep(9)
print("Daniel is a good boy")

input()
