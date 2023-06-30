
# Write a program that asks a user for their name and prints it in the following
# funny pattern
name = input('Enter your name: ')
count = ''
for i in name:
    count = count+i
    print (count)

input()

#Write a program that asks the user to enter a string, then print out each letter
# of the string doubled on a seperate line.
str = input('Enter a string: ')
for c in str:
    print (c*2)
input()



#Write a program that ask the user for a string
str=input('Enter a string: ')
for i in range(len(str)):
    if str[i]=='e':
        print('str[',i,']',sep='')
input()



#Write a program that prints out every character before an 'a' in the word 'Cananda'
w='Canada'
for i in range(len(w)):
    if w[i]=='a':
        print(w[i -1])
input()

#Write a program that extract the memory location of
f='Banana'
for i in range(len(f)):
    if f[i]=='a':
        print(i)
input()


s='Power'
for c in s:
    print(c)
input()

s='Power'
for i in range(len(s)):
    print(s[i])
input()

s='Flower'
print('P'+s[2:])

input()

name=input('Enter a string: ')
word='CANADA'
nat=word[:5]+name
print('Natinality:',nat)

input()

name='CANADA'
print(name[-3:])
print(name[3:])
print(name[3:6])
name2=name[::-1]
print(name2[:3])
print(name[1]+name[4:])
print(name[-1:-4:-1])
print(name[-1::-2])
input()


#Write a Program which counts how many of the squares of numbers from 1 to 100 end in a 4
count = 0
for i in range(1,101):
    num=i**2
    if num%10==4:
        count+=1
print(count)
input()
#Write a program that asks the user to enter a word and determine if it is a panlidrome
s = input('Input a word: ')
if s != s[::-1]:
    print(str(s), 'is not a a panlidrome')
else:
    print(str(s),"is a panlidrome")

input()

# Ask the user for a number and then print print out the the following, where the patterns ends at the number
#the user enters
s = 0
num = eval(input('enter a number:'))
for i in range(num):
    s = s+1
    print(' '*s,s)

input()

from string import punctuation,printable,digits

sentence = "He's too shy! I don't like him. Any other guy?"
for c in punctuation:
    sentence = sentence.replace(c,'')
print(sentence)

# print(punctuation)
# print('---------------------------------------------------------')
# print(printable)
# print('---------------------------------------------------------')
# print(digits)

input()


# Accept a user statement and output:
# 1. First character of the string
# 2. The first 3 characters of the string
# 3. The last 3 characters of the string
# 4. The string backwards
# 5. 7th character of the string if the strimg is long enough or a message otherwise.
char = input('Enter a Character: ')
print(char[0])
print(char[:3])
print(char[-3:])
print(char[::-1])
if len(char)< 7:
    print('The character inputed is not long enough')
else:
    print(char[6])

input()

s = 'abcdefghij'
print(s[2:5])
print(s[:5])
print(s[5:])
print(s[-2: ])
print(s[:])
print(s[1:6:2])
print(s[::-1])
input()

root = "Dandelion"
print(root[:3])
print(root[-4: ])

input()

# Create a program that accepts a string input, Generate a random index between 0 & 20.
# Random Index should display a character if it does exist. if it doesn't, a message
# should be displayed to such effect.
from random import randint
str = input('Enter a string: ')
for i in range(4):
    randindex = randint(0,9)
    print(str[randindex], end='')

input()

userstr = input('Write something: ')
print(userstr[-2])
print(userstr[2])

input()

s = 'PYTHON'
print(s[0])
print()
print(s[3])
print()
print(s[1])
print()

print(s[-1])
print()
print(s[-2])

input()

s = ''
for i in range(7):
    t = input('Enter a letter: ')
    if t in 'aeiou':
        s+= t
print (s)

input()

a = 'Hello! Space exists'
if ' ' in 'i want soup':
    print (a)

input()

str = 'Banana'
if 'f' not in str:
    print('Absent')

input()

str = 'Banana'
if 'f' in str:
    print('Your string contains the letter a.')
else:
    print('Not in string')

input()

s = ''
for i in range(7):
    t = input('Enter a letter: ')
    if t== 'a' or t=='e' or t=='i' or t=='o' or t=='u':
        s+= t
print (s)

input()

s = ''
for i  in range (4):
    c = input("Enter character: ") + " "
    s += c
print(s)

input()

s = ""
for i  in range (4):
    c = input("Enter character: ")
    s = s+c
print(s)

input()

# Write a prpgramme that asks a user to enter a string.
# The program should list the number of char in the
# string and repeat it 10 times

string = input('Enter a String: ')
print(len(string))
print(string * 10)

input()

print('AB'+'cd')
print('A'+'7'+'B')
print('Hi'*4)
print(len('Hi'))

input()

n = "She is crazy"
t = 'He is stupid'
print (n)
print(type(n))
print (t)
print (type(t))

input()

cur_time = "The time is 8 0'clock"
print(cur_time)