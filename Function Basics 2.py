#TRAPEZIUM PROGRAM

def drawTrap(b,f):
    for i in range(b,f):
      print("*" * i)

drawTrap(15 , 30)

input()
#Write a function program that accepts 3 different arguments: name,age and occupation and outputs
def processUser(name,age,occupation):
    if occupation == "Agent":
        print(name, " You belong to Real Estate Sector")
        print("In 5 yrs: ", age + 5)
    elif occupation == "Chef":
        print(name, "You belong to the Hospitality Sector ")
        print("In 5 yrs: ", age + 5)
    elif occupation == "Web Designer":
        print(name, "You belong to the ICT Sector")
        print("In 5 yrs: ", age + 5)

processUser('Felix', 22, 'Chef')
print("--------------------------------")
processUser('Hyunjin', 23, 'Web Designer')
print("--------------------------------")
processUser('Chan', 25, 'Agent')
input()


#Write a function program that given a variabe program x = 4, increments the value of x by 3 and returns the results.
#method 1
def incrementX():
    x = 4
    return x + 3
print(incrementX())

#method 2
def incrementX(x):
    return x + 3
print(incrementX(4))
input()
def convert(t):
    return t*9/5+32
#print(convert(20))
print(convert(20) + 5)
print(convert(20 + 5))
input()


def multiple_string(string,n):
    print(string*n)
    print()
multiple_string('Hello',5)
multiple_string('A',10)
input()



def hello(n,s):
    print("hello "*n,s)
hello(5,3)


def hello(n):
    print("Hello "*n)
hello(5)

hello(10)

print(4,5)

def draw_rect():
    print("*"*20)
    print('*',' '*16,'*')
    print('*',' '*16,'*')
    print("*"*20)
draw_rect()
input()

def hello():
    print("hello!")


hello()