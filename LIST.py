from random import randint

mypets = ['tom','charlie','muffy','dan','goldie']
ashlist= [len(x)*'#' for x in mypets]
print(ashlist)

input()
n=[3500,6000,10000,14000,7000]
newN= ['$'+str(i) for i in n]
print(newN)
input()

bn = [str(randint(0,1)) for i in range(5)]
print(''.join(bn))

input()
l = []
for i in range(5):
    l= l + [str(randint(0,1))]
l= "".join(l)
print(l)

input()
print([even for even in range(20,31) if even%2==0])

input()
M = ['one', 'two', 'three', 'four', 'five', 'six']
newM = [i for i in M if 'o' in i]
print(newM)

input()
speed = [20,50,35,3,70]
time = 5
distance = [item * time for item in speed]
print(distance)

names_students = ['remi', 'kunle', 'peter', 'pat', 'temi']
lengths = [len(x) for x in names_students]
print(lengths)
input()
string = 'Hello'
L = [1,14,5,9,12]
M = ['one', 'two', 'three', 'four', 'five', 'six']

print([0 for i in range(10)])
print([i**2 for i in range(1,8)])
print([i*10 for i in L])
print([c*2 for c in string])
print([m[0] for m in M])
print([i for i in L if i<10])
print([m[0] for m in M if len(m) == 3])
input()
# l = [returnValue for loop if statement]

l = [i for i in range(5)]
t = [i for i in range(5) if i % 2 == 0]

print(l)
print(t)
input()


clubs =[]
for i in range(4):
    club = input("Enter a club: ")
    clubs.append(club)
print(clubs)

for j in range(len(clubs)):
    clubs[j] = clubs[j][1: ]
print(clubs)

input()


str_list=[]
for i in range(6):
    str = input("Enter String here: ")
    hand  = str[1:len(str)]
    str_list.append(hand)
print(str_list)


input()
alphas ='abcdefghijklmnopqrstuvwxyz'
copies =[]

for i in range(len(alphas)):
    copies.append(alphas[i] * (i+1))
print(copies)
input()

num2 =[]
count =1
for i in range(50):
    num2.append(count**2)
    count += 1
print(num2)
input()
num =[]
count =0
for i in range(50):
    num.append(count)
    count += 1
print(num)
input()

l = []
for i in range(50):
    # l.append(randint(1,100)) #alternative

    l = l + [randint(1,100)]
print(l)
input()

cars= ['toyota', 'acura', 'range', 'porshe', 'sport']

cars.insert(2,'benz')
cars.insert(5,'mazda')
print(cars)
cars.pop(3)
cars = cars + ["lexus"]*3
print(cars)

cars.count("lexus")
print(round(cars.count("lexus")/len(cars)*100,1))
input()
l = [6,7,8]
l[1] = 9
print(l)        #output [6,9,8]
l.insert(1,9)
print(l)        #output [6,9,9,8]
del l[1]
print(l)        #output [6,9,8]
del l[:2]
print(l)        #output [8]

input()
cars =['Lexus', 'aston martin', 'bugatti']
print(cars)
new_cars = ["Dodge","F1"]
cars.extend(new_cars)
print(cars)
cars.pop()
print(cars)
# x = 'Lexus'
# y = 'aston martin'
# z = 'Lexus again'
# cars.append(x)
# print(cars)
# cars.append(y)
# print(cars)
# cars.append(z)
# print(cars)


input()
scores =[45,90,66,23,56,87,42]
pass_scores =[]
for i in range(len(scores)):
    if scores[i] > 50:
        pass_scores.append(scores[i])
print(pass_scores)
input()
scores =[45,90,66,23,56,87,42]
scores.sort()
print(scores[:2])
print(scores[-2:])

input()
l = ["Taiwo","Kehinde"]
t = l[ : ]
print(t)

input()

integers =[70,41,22,90,57]
print(round(sum(integers)/len(integers)))
print()
input()
#count how many items in a list named integers are greater than 50
integers =[70,41,22,90,57]
count =0
for i in range(len(integers)):
    if integers[i] > 50:
        count+=1
print(count)
input()

alpha ="abcdefghijklmnopqrstuvwxyz"

for i in range(26):
    print(alpha[i: ] + alpha[ :i],)

input()

a =[10,3,5]
b=[10,3,2]
n=[]
for i in range(len(a)):
    n.append(a[i] + b[i])

print(n)
input()


print(max([10,13,17]))
print(min([10,13,17]))
input()

m = [2,3,4,5,6]
for i in range(len(m)):
    m[i]= m[i]**2
print(m)



input()
print([7,8] + [3,4,5])
print([7,8] * 3)
print([0]*5)

m = [1,9,4,5] + [0]*7
print(m)
input()
l = [6,7,8,9,6]
print(l[0])
print(l[:3])
print(l.index(8))
print(l.count(6))
input()



input()

l = [1,2,3]
print(type(l))
print(isinstance(l,list))

nums= [0,1,2,3,4,5,6,7,8,9,10,
       11,12,13,14,15,16,17,18,19,20]
l =[1, 2.718, 'abc', [5,6,7]]
l.append(0)
print(l)
if 0 not in l:
    print("Your list has no zeroes")


print(l[0])
print(l[2])
print(l[3])
print(l[3][2])