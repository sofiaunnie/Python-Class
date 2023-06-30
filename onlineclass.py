def highest_even(li):
    c = 0
    for i in li:
        if i % 2 == 0:
            if i > c:
                c = i
    print(c)


print(highest_even([10,2,3,4,8,11]))

input()

def checkDriverAge(age=0):

    if int(age) < 18:
        print("Sorry, you are too young to drive this car. Powering off")
    elif int(age) > 18:
        print("Powering On. Enjoy the ride!")
    elif int(age) == 18:
        print("Congratulations on your first year of driving. Enjoy the ride!")
checkDriverAge(92)
input()
input()


some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

some_list.sort()

for i in some_list:
    if(some_list[0] == some_list[1]):
        some_list.pop(1)
    else:
        print("No duplicate")

input()

picture =[
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]

for i in picture:
    for ii in i:
        if ii == 1:
            print('*', end='')
        else:
            print(' ', end='')
    print('')



for i,char in enumerate(list(range(100))):
    if i == 50:
        print(f'the index of {i} is {char}')


input()
my_list = [1,2,3,4,5,6,7,8,9,10]
count = 0
for i in my_list:
    count = count + i
print(count)
input()
a = '25'
b = '35'
# print(f'{(a)+(b)} answer ')

def function(a,b):
    print(a + b)
function(a,b)


is_magician = False
is_expert = True

if is_magician == True and is_expert == True:
    print('You are a master magician')
elif is_magician == True or is_expert == True:
    print('at least you are getting there')
else:
    print('you need magic power')
input()
my_tuple = [1, 2, 3, 4, 5, 5]
new_my_tuple = set(my_tuple)

print(my_tuple)
print(new_my_tuple)
