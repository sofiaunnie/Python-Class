# # Palindrome
# for i in range(2):
#     str = input('Enter a word: ')
#     if str != str[::-1]:
#         print("This is not a Palindrome")
#
#     else:
#         print("This is a Palindrome")
#         break
#
# input()
#
# str = input('Enter a String: ')
# new = ''
# for i in range (len(str)):
#     print(str[1::2].upper)
#
# input()
#
# # Write a program that asks the user to enter a word and then capitalize every other letter
# # of that word. so if the user enters the string 'rhinocerous', the program should print 'rHiNoCeRoS'.
# str = input('Enter a string: ')
# word = ''
# for i in range (len(str)):
#     if i % 2 == 0:
#         word += str[i].lower()
#     else:
#         word += str[i].upper()
# print (word)
#
# input()
#
#
#
#
# # How would you get this output using python program.
#
# #Method 2
# name = input("Enter name: ").title()
# name1 = name[:name.index(' ')]
#
# print('Dear', name)
# print("I am pleased to offer you our new Platinum Plus Rewards card at a special\n"
#       "introductory APR of 47.99%."+" "+str(name1)+", an offer like this does not come along\n"
#       "everyday, so i urge you to call now toll-free at 1-800-314-1592. We cannot offer\n"
#       "such a low rate for long,"+" "+str(name1)+", so call right away" )
# input()
#
#
#
# # Method 1
# name = input("Enter name: ").title()
# names = name.split()
#
# print('Dear', name)
# print("I am pleased to offer you our new Platinum Plus Rewards card at a special\n"
#       "introductory APR of 47.99%."+" "+str(names[0])+", an offer like this does not come along\n"
#       "everyday, so i urge you to call now toll-free at 1-800-314-1592. We cannot offer\n"
#       "such a low rate for long,"+" "+str(names[0])+", so call right away" )
# input()
#
#
# print('-'.join("1 225 3140".split())) #Split and join together
#
# input()


n = ' 1 225 3140'
s = '1-225-3140'
splitted_n = n.split()
splitted_s = s.split('-')
print(splitted_n)
print(splitted_s)

input()


s = "We are several topics away from finishing the python course"
splitted_s = s.split()
print(splitted_s)

input()

# Write a programe that ask a user in lowercase and then
# capitalize the first letter of each word of their name

# Method 4: SPLIT THE STRING INTO ITS WORD (LIST ITEMS)
name = input("Enter a string: ")
nameslist = name.split()
nameslist = [item[0].upper() + item[1:] for item in nameslist]
print(nameslist)

newname = ' '.join(nameslist)
print(newname)

input()

#Method 1
fullname = ""
for i in range(3):
    name = input("Enter name: ")
    fullname = fullname + name.title() + ' '
print(fullname)

input()

#Method 2: USE TITLE CASE ON THE ENTIRE STRING
name = input("Enter a string: ")
nametitled = name.title()
print(nametitled)

input()

#Method 3
fullname =""
for i in range(3):
    name = input('Enter your names: ').title()
    fullname = fullname + name + ' '
print(fullname)
input()


for i in range(1):
    str1 = input("Enter a string: ")
    str2 = input("Enter a string: ")
    if len(str1) != len(str2):
        print("Unequal lengths !")
        break
    else:
        newstring = ''
        finalstring = ''
        for i in range(len(str1)):
            newstring = str1[i].upper() + str2[i].lower()
            finalstring = finalstring + newstring
        print(finalstring)
input()

#
code = input("Enter text: ")
e_code = ''
for c in code[::2]:
    e_code+=c
for c in code[1::2]:
    e_code+=c
print(e_code)
input()

# Write a program that, given a string that contains a decimal number,
# print out the decimal part of the number.
num = input("Enter a Number: ")
print(num[num.index(".")+1:])
input()

num = 12
print(f"int: {num:d}; hex: {num:x}; oct: {num:o}; bin: {num:b}")
input()

alphabet = 'abcdefghijklmnopqrstuvwxyz'
key ='xznlwebgjihqdyvtkfuompciasr'
secret_message = input("Enter your message:")
secret_message = secret_message.lower()
for c in secret_message:
    if c.isalpha():
        print(alphabet[key.index(c)], end=' ')
    else:
        print(c, end=' ')
input()

alphabet = 'abcdefghijklmnopqrstuvwxyz'
key ='xznlwebgjihqdyvtkfuompciasr'
secret_message = input("Enter your message:")
secret_message = secret_message.lower()
for c in secret_message:
    if c.isalpha():
        print(key[alphabet.index(c)], end=' ')
    else:
        print(c, end=' ')
input()

#RHOMBUS PROGRAM
r = int(input("Enter length of diagonal of rhombus: "))
for i in range(r):
    print(('*'* i).rjust(r) + '*' + ('*'* i).ljust(r))
for i in range(r,-1,-1):
    print(('*'* i).rjust(r) + '*' + ('*'* i).ljust(r))
input()

print('*'.rjust(10))
print(len('**'.rjust(10)))
print('**'.rjust(10))
print(len('**'.rjust(10)))
print('*'.rjust(10) + '*' + '*'.ljust(10))
print(len('*'.rjust(10) + '*' + '*'.ljust(10)))
print('**'.rjust(10) + '*' + '**'.ljust(10))
print(len('**'.rjust(10) + '*' + '**'.ljust(10)))
input()

str = input("Enter any string: ")
trio = str[-3: ]
rev = trio[ : :-1]
print("Last three chars: ", trio)
print("last three reversed: ", rev)
quadupled_s =" "
if trio == "ing":
    for c in rev:
        quadupled_s = quadupled_s +c * 4
print(quadupled_s)
new_s = quadupled_s.replace("n","@")
print(new_s)

input()

email = input("Enter email address: ")
print(email[email.index("@")+1 : ])

for i in range(2):
    password = input("Enter a password: ")
    if not password.isalnum():
        print(password + "is: "+" strong")
    else:
        print(password + "is: "+" strong")
input()

print(len(input("Enter a word: ").split()))
input()
count = 0
string = input("Enter a sentence: ")
for i in string:
    if i == " ":
        count += 1
print("Number of space: ", count)
print("Number of words:", len(string.split()))
print("Number of words: ",count(" ")+1)
input()


# Write a program that accepts a string sentence and counts the number.
# a. Spaces in the string
# b. words in the string

str = input("Enter a string: ")
print("There are",str.count(' '), "spaces in the string")
print("There are",len(str.split()), "words in the string")

input()

# Write a program that validates a user's password input. if there are any
# special characters in the password, let user know they have a strong password.
# If there aren't they should know their password is weak.
pwd = input("Enter your password: ")
if pwd.isalnum():
    print("Your password is Weak")

else:
    print("Your password is Strong")

input()


p = input("Enter your password: ")
if not p.isalnum():
    print("Password Invalid!")

else:
    print('Welcome User!')
input()

# A string phone is ='1-505-4530'. using if statements and string methods. write a program that:
# a. replaces every hyphen(-) with an ash (#) in a new string p and display p
# b. that can output 15054530 from phone
# c. if string phone is now changed or modified to '1-505-4530z', write some code that prints "NUMBER INVALID"
# d. if string phone is now changed or modified to '
# message in uppercase characters only, if a letter 'Z' is added to our phone string AND also output
# the location/index of '1-505-4530ZAB', output all invalid indexes A,B & Z

# a
num = '1-505-4530'
p = num.replace('-', '#')
print (p)

# b
print(num.replace('-',''))

# c
n = num +"Z"
if n.isdigit:
    print('Number Valid:'.upper(), 'invalid char at index', n.index('Z'))

# d
num = '1-505-4530ZAB'
for i in range(len(num)):
    if num[i].isalpha():
        print(i)
input()

# Write code that accepts name inputs and prints out your name(initially in lower case),
# all in uppercase characters
n = input('Enter your name werey!: ').upper()
print(n)

input()

s = '45mins'
t = '45'

print(s.isdigit())        # False
print(t.isdigit())        # True
print(s[0].isdigit())     # True
print(s[1].isdigit())     # True
print(s[2].isdigit())     # False


input()

s = input('Enter a string: ')
if s[0].isalpha():
    print('Your string starts with a letter')
if not s.isalpha():
    print("Your string contains a non-letter.")

input()

s = '1-505-4530ZW'
for i in range(len(s)):
    if s[i].isalpha():
        print(i)

input()

# s = "Hi Guys! Wendy says Hi too. Say Hi also if you get our messages"
# print(s.count(' '))   counts the string
# s = s.replace("Hi", "Hello")  replaces "Hi" with "Hello" in the string
# print(s)
# s = s.upper()                  Returns as Uppercase
# print(s)
# print(s.index('A'))            returns the index number of a string
# input()

print(s.upper())
s = (s.replace('Hi', 'Hello'))
print(s)
print(s.count(' '))
print(s.index(' '))

input()
s = 'Chicken'
print (s)
print(s.lower())
print(s)
s = s.lower()
print(s)

print()


# Write a program that asks a user for their name and prints it in the following
# funny pattern
n = input("Enter your name: ")
for i in range (len(n)):
    print(n[:i+1], end =' ')
input()
