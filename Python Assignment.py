
from random import randint
x = str(randint(1,10))+"."+str(randint(0,9))+str(randint(0,9))
decimal = float(x)
print(decimal)
print(decimal*10)
print(type(decimal))
input()

for i in range(50):
    print(randint(3,6),end="")