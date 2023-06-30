from random import randint
str = input("Enter any string: ")
print(str[:1])
print(str[:3])
print(str[-3:])
print(str[::-1])
if len(str) > 6:
    print(str[6])
else:
    print("String is not long enough")

input()

s = 'abcdefghij'
print(s[2:5])
print(s[:5])
print(s[5:])
print(s[-2:])
print(s[:])
print(s[1:6:2])
print(s[::-1])
input()

root = "Dandelion"
print(root[:3])
print(root[-4:])
input()

#let user input in a sting, Generate a random index  btw 0 to 15

from random import randint
str = input("Enter any string: ")
for i in range(5):
    x = randint(0,15)
    print(str[x]," : ",x)
input()

from random import randint
str = input("Enter any string: ")
for i in range(4):
    x = randint(0,9)
    print(str[x], end='')
input()

