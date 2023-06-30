

user = 'canada'
for i in range(len(user)):
    if user[i] == 'a':
        print(user[i-1])
input()


#not keeping track
user = 'canada'
for i in user:
    if i != 'a':
        print(i)
input()


#keeping track
user = input("enter a word: ")
for i in range(len(user)):
    if user[i] == 'e':
        print(i)
input()
input()





f = 'Banana'
for i in range(len(f)):
    if f[i] == 'a':
        print(i)
input()
s= 'flower'
s= 'p' + s[2:]
for c in s:
    print(c)

input()

s= 'flower'
s= 'p' + s[2:]
for i in range(len(s)):
    print(s[i])

input()
num = 1
user = eval(input("Enter a number: "))
for i in range(user):
    print(" " * num, num)
    num = num + 1

input()


user = input("Enter a Palindrome Word: ")
if user[::] == user[::-1]:
    print('This word is a Palindrome Word')
else:
    print('This word is not a Palindrome Word')
input()
input()


count = 0
for i in range(1,1000):
    i = i * i
    if i % 10 == 4:

        count += 1
print(count)
input()
input()



s= input("Enter a word: ")
nationality = s[:5] + 'ian'
print(nationality)

input()

s= "canada"
print(s[3:])
print(s[-3:])
print(s[-1:-4:-1])
print(s[3:6])
print(s[3]+s[4]+s[5])
print(s[3]+s[4:6])
print(s[-1::-2])

input()
s = input('Enter a string')
print(s[0] + "*" + s[2:] + '!' * 3)

input()

count = 0
for i in range(1,1000):
    i = i * i
    if i % 10 == 4:
        count += 1
print(count)
input()
input()

user = input("Enter a Palindrome Word: ")
if user[::] == user[::-1]:
    print('This word is a Palindrome Word')
else:
    print('This word is not a Palindrome Word')
input()
input()


num = 1
user = eval(input("Enter a number: "))
for i in range(user):
    print(" " * num, num)
    num = num + 1

input()
from string import punctuation,printable,digits

sentence = "He's too shy! I dont like him. Any other guy?"
for c in punctuation:
    sentence = sentence.replace(c,'')
print(sentence)

# print(punctuation)
# print('------------------')
# print(printable)
# print('------------------')
# print(digits)

input()
from random import randint
user = input('Enter a text:')
usernum = len(user)
print(user[0])
print(user[:3])
print(user[-3:])
print(user[::-1])
if usernum <= 7:
    print("too short")
else:
    print(user[6])




input()

s='abcdefghij'
print(s[2:5])
print(s[:5])
print(s[5:])
print(s[-2:])
print(s[:])
print(s[1:6:2])
print(s[::-1])

input()
root = 'Dandelion'
print(root[:3])
print(root[-4:])
input()


str = input("Enter any string:")
for i in range(4):
    x =randint(0,9)
    print(str[x], end='')


input()
user = input("Enter a text: ")
userNum =len(user)

for i in range(5):
    num = randint(0, 15)
    print(num)
    if userNum < num:
        print("Index do not exist")

    else:
        print(user[num])

input()

user = input('Enter a 6 letter word: ')
if len(user) < 6:
    print("too short")
else:
    print('second to the last number ',user[-2].upper(),'second to number ', user[2].upper())

input()
s= 'Python'
print(s[0])
print()
print(s[1])
print()
print(s[-1])
print()
print(s[-2])

print(s[-5])


input()
s= ''
for i in range(7):
    t=input('Enter a letter')
    if t in 'aeiou':
        s=s+t
print(s)

input()

a= 'Hello! Space exists'
if '' in 'i want soup':
    print(a)


input()
str = 'banana'
if 'f' not in str:
    print('Absent')
else:
    print('present')


input()

str = 'banana'
if 'f' in str:
    print('Your string contains the letter a.')
else:
    print('Not in string')


input()
s= ''
for i in range(7):
    t=input('Enter a letter')
    if t =='a' or t =='e' or t =='i' or t =='o' or t =='u':
        s=s+t
print(s)

input()
statement =''
for i in range(4):
    text= input('Enter a word: ') + " "
    statement= statement + text
print(statement)



input()
print(len('hi  '))
input()

s= ''

for i in range(4):
    c= input('Enter char')
    s= s+c
print(s)

input()


user = input('Enter a text: ')
print('The total number of the text is', len(user))
print(user * 10)

input()
print('ab' + 'cd')
print('a' + '7' + 'b')
print('Hi' * 4)
print(len('hi'))

input()
n="She is crazy"

t='He is Stupid'

print(type(n))
print(type(t))

time = ("the time is 8 o'clock")
print(time)
