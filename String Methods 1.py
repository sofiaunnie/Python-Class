#THE SPLIT AND JOIN METHODS
f_name = input("Enter fullname: ")
f_name_s = f_name.split()
print("Dear " + f_name +
      ",i am pleased to offer you our new Platinum Plus Rewards card at a special introductory APR of 47.99%." +
      f_name_s[0] + ", an offer like this does not come along everyday, so i urge you to cal now toll free at" +
      "1-800-314-1592. We cannot offer such a low rate for long," + f_name_s[0] + ", so call right away.")
input()
print('-'.join("1 225 3140".split()))
input()

"1 225 3140".split()
"1-225-3140".split("-")
s = "We are several topics away from finishing the python course"
splitted_s = s.split()
print(splitted_s)
input()

#Write a program that asks the user to enter their name in lowercase and then capitalizes the first letter of each
# word of their name

#METHOD 1 - Using TitleCase Method

fullname = ""
for i in range(3):
      name = input("Enter name: ")
      fullname = fullname + name.title() + " "
print(fullname)

#METHOD 2 - Using Title Case on the entire string
name = input("Enter Name: ")
nametitled = name.title()
print(nametitled)

#METHOD 3 -
fullname = ""
for i in range(3):
      name = input("Enter name: ").title()
      fullname = fullname + name + " "
print(fullname)

#METHOD 4 - SPLIT THE STRING INTO ITS WORDS(LIST ITEMS)
#The method is known as the list comprehension
name = input("Enter a string: ")  #enter string
nameslist =name.split()           #splits a string into words
nameslist = [item[0].upper()+item[1:] for item in nameslist]
#capitalize first letter of items in list,returns
print(nameslist)
newname = " ".join(nameslist)     #join with space
print(newname)
input()


for i in range(1):
    str1 = input("Enter a string: ")
    str2 = input("Enter second string: ")
    str1 = str1.upper()
    if len(str1) != len(str2):
        print("Unequal lengths !")
        break
    else:
        newstring = ""
        finalstring = ""
        for i in range(len(str1)):
            newstring = str1[i] + str2[i]
            finalstring = finalstring + newstring
        print(finalstring)
input()

# SUBSTITUTION CIPHER
#encode
alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = 'xznlwebgjhqdyvtkfuompciasr'
secret_message = input('Enter your message:')
secret_message = secret_message.lower()
for c in secret_message:
    if c.isalpha():
        print(key[alphabet.index(c)],end='')
    else:
        print(c,end='')

#decode
alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = 'xznlwebgjhqdyvtkfuompciasr'
secret_message = input('Enter your message:')
secret_message = secret_message.lower()
for c in secret_message:
    if c.isalpha():
        print(alphabet[key.index(c)],end='')
    else:
        print(c,end='')

input()

#RHOMBUS PROGRAM
b = int(input("Enter length: "))
for i in range(b):
    print(('*'*i).rjust(b) + '*' + ('*'*i).ljust(b))
for i in range(b,-1,-1):
    print(('*' * i).rjust(b) + '*' + ('*' * i).ljust(b))

input()

#String Methods RJUST AND lJUST
print('*'.rjust(10))
print('*'.rjust(10).count(' '))
print('**'.rjust(10))
print('**'.rjust(10).count(' '))
print(len('*'.rjust(10)))
print(len('**'.rjust(10)))
print('*'.rjust(10) + '*' + '*'.ljust(10))
print(len('*'.rjust(10) + '*' + '*'.ljust(10)))
print('**'.rjust(10) + '*' + '**'.ljust(10))
print(len('**'.rjust(10) + '*' + '**'.ljust(10)))
input()

str=input("Enter a string: ")
trio = str[-3: ]
rev = trio [ ::-1]
print("Last three chars: ",trio)
print("Last three reversed: ",rev)
quadrupled_s = ""
if trio == "ing":
    for c in rev:
        quadrupled_s = quadrupled_s + c * 4
print(quadrupled_s)
new_s = quadrupled_s.replace("n","@")
print(new_s)
input()

from string import punctuation,printable,digits

user2 = input("Enter strings: ")
s= user2[-1:-4:-1]
print(s)
#user2 = input("Enter strings: ")

if user2[-3:] == "ing":
    print(user2[-1:]*4,user2[-2]*4,user2[-3]*4, sep='')


# Write out a program that prints out everything after the @ symbol
# in any email address
email =input("Enter Email address:")
print(email[email.index("@")+1: ])
input()

# for i in range(2):
#     password = input()
#
# s = input("Enter a string sentence")
string =input("Enter a string: ")
count_space = 0
count_word = 0
for i in range(len(string)):
    if string[i] ==" ":
        count_space +=1
    elif string[i].isalpha():
        count_word +=1
print("There are",count_word,"words",count_space,"spaces")

input()
input()

user = input("Enter a password: ")

if not user.isidentifier() and not user.isdigit():
    print("Very Strong")
else:
    print("Not strong")

input()
input()

phone = input('Enter a password')
if phone.isalnum():
    print('Valid Password')
else:
    print("Invalid password")
input()
input()
phone = '1-505-4530ZAB'
for i in range(len(phone)):
    if phone[i].isalpha():
        print(i)
input()
phone = '1-505-4530'
print(phone.replace('-', '#'))
print(phone.replace('-', ''))
phone = '1-505-4530Z'
if 'z' in phone:
    print('NUMBER INVALID',phone.index("Z"))
print()


phone = '1-505-4530'
if phone.isdigit() == False:
    print(phone.replace('-','#'))
if phone.isdigit() == False:
    print(phone.replace('-',''))

phone= phone.replace('1-505-4530','1-505-4530Z')
if phone.isdigit() == False:
    print('number invalid'.upper())
    for i in range(len(phone)):
        if phone[i].isalpha() == True:
            print(i)

input()

user = input('Enter your name: ')
print(user.upper())


input()

s = '45mins'
t = '45'
print(s.isdigit())
print(t.isdigit())
print(s[0].isdigit())
print(s[1].isdigit())
print(s[2].isdigit())

input()
s= input("Enter a string")
if s[0].isalpha():
    print("Your string starts with a letter")
if not s.isalpha():
    print("Yor string contains a non-letter")

input()
s= '1-505-4530ZW'
for i in range(len(s)):
    if s[i].isalpha():
        print(i)

s = "Hi Guys! Wendy says Hi too. Say Hi also if you get our messages"
print(s.upper())
print(s.replace('Hi','Hello'))
print(s.count(' '))
print(s.index(' '))

input()




s = "Hi! Guys! Wendy says Hi too. Say Hi also if you get our messages"
print(s.count(' '))
s = s.replace('Hi','Hello')
print(s)
s = s.upper()
print(s)
print(s.index('A'))

input()
s = 'CHICKEN'
print(s)
print(s.lower())
print(s)
s = s.lower()
print(s)

input()

#method                         Description
#lower()                        return lower case
#upper()                        return every letter in upper case
#replace(x,y)                   replace every occurance of x with y in a string
#count(x)                       count the number of time x occur
#index()

user = input('Enter your name: ')
for i in range(len(user)+1):
    print(user[:i], end=' ')

input()

user = input('Enter a string: ')
for i in user:
    print(i * 2)
input()
input()
