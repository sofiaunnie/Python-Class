#SETS
L = [3,8,9,4,8,7,3,9,0,4,6,7,1,2,7,6,0]
unique = list(set(L))
print("Unique List: ",unique)
frequencies = [L.count(item) for item in unique]
print("Ftequencies: ",frequencies)

myset = {3,5,"money",98.5 ,"money",5}
l = {1,5,5,'V','N','A','A','T'}
m = 'Access'

print(set(m))
print(set(l))

print('---------------------------------------------------------------------------')


print(myset)
print(type(myset))

input()

#Multiple Choices From a list

from random import randint
from string import printable
#print(printable[randint(0,98)])

#myssh = ""
#for i in range(451):

input()

from random import choices
from string import printable
#print(printable[ :-2])
ssh_char = printable[printable.index('0'): printable.index('!')]
ssh_key = ''.join(choices(ssh_char,k=451))
print(ssh_key)

input()

#classwork 1
# create a function called generate_puzzle that generates a word puzzle. Puzzle generated by the function
# should be 8 letters wide and 9 rows high
from random import choices
from string import printable
#print(printable)
puzzletters = printable[printable.index('A'): printable.index('Z')+1]
#print(puzzletters)
def generate_puzzle(letters):
    for i in range(9):
        sequence = choices(letters,k=8)
        print(' '.join(sequence))
generate_puzzle(puzzletters)
input()

#example
from random import choices
colors = ['red','pink','peach','black','blue','cream','brown','white','wine','scarlet','gold','violet']
mycolors = choices(colors, k= 5)
print(mycolors)

input()

from random import randint
L = [1,14,5,9,12]
L_str = ''.join([str(x) for x in L])
L_str = int(L_str)
print(L_str)
print(type(L_str))
input()

#LIST COMPREHENSION
mypets = ['tom','charlie','muffy','dan','goldie']
ashlist = [len(x)*'#' for x in mypets]
print(ashlist)
input()

N =[3500,6000,10000,14000,7000]
amounts = ['$'+ str(i) for i in N]
print(amounts)
input()

#method 1
from random import randint
bn = [str(randint(0,1)) for i in range(5)]
print(''.join(bn))
input()
#method 2
from random import randint
bin=[]
for i in range(5):
    bin = bin + [str(randint(0,1))]
print(''.join(bin))
input()

even = [i for i in range(20,31) if i%2==0 ]#
print(even)
input()

L = [1,14,5,9,12]
M = ['one','two','three','four','five','six']
numbers = [item for item in M if 'o' in item]
print(numbers)
input()

n = [0 for i in range(10)]
print(n)
input()

M = ['one','two','three','four','five','six']
n = [m[0] for m in M]
print(n)
input()

speed =[20,50,35,3,70]
time = 5
distance = [item * time for item in speed]
print(distance)
input()
#The l
alphas = "abcdefghijklmnopqrstuvwxyz"
copies=[]
for i in range(len(alphas)):
  copies.append(alphas[i]*(i+1))
print(copies)
input()

#A list containing the squares of the integers 1 through 50.
l=[]
for i in range(1,51):
   l.append(i*i)
print(l)
input()

#A list consisting of the integers 0 through 49.
l=[]
for i in range(50):
 l.append(i)
print(l)
input()

#To generate 50 random numbers between 1 to 100
#Method 1
from random import randint
L = []
for i in range(50):
    L.append(randint(1,100))
print(L)

#Method2
from random import randint
L = []
for i in range(50):
    L = L +[randint(1,100)]
print(L)
input()

cars = ['toyota','acura','range','porsche','sport']
cars.insert(2,'benz')
cars.insert(5, 'mazda')
del cars[3]
cars = cars + ['lexus']*3
print(cars)
print(round(cars.count('lexus')/len(cars)*100,1))
input()

L = [6,7,8]
#L[1]=9         output: [6,9,8]
#L.insert(1,9)  output:[6, 9, 7, 8]
#del L[1]        output: [6, 8]
#del L[ :2]  output:[8]

print(L)

input()
cars =[]
x = 'Lexus'
y = 'aston martin'
z = 'Toyota'
cars.append(x)
print(cars)
cars.append(y)
print(cars)
cars.append(z)
print(cars)

new_cars =["Dodge","F1"]
cars.extend(new_cars)
print(cars)

cars.pop()
print(cars)
input()

#Write a program that prints out the two largest nd two smallest elements of a list called scores.
#scores=[45,90,66,23,56,87,42]
#secondly,create a new list called pass_scores from this scores list of all listed scores that are greater than 50.

scores = [45,90,66,23,56,87,42]
scores.sort()
print(scores)
#input()
print("Largest are:",scores[-2:])
print("Smallest are:",scores[0:2])
#pass_scores =
