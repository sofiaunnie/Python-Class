from random import randint

covid = open("covid_patient.txt","w")
for i in range(6):
    patient_name = input('Enter patient name: ').upper()
    patient_num = randint(100,999)
    patient_ID = patient_name[ :3].upper() + str(patient_num)
    print(patient_ID)
    patient_temp = eval(input("Enter patient temperature: "))
    if patient_temp > 40:
        covid.write(f"{patient_name} {patient_ID} {patient_temp} \n")
covid.close()
input()

f = open('fahtemps.txt','w')
temperatures = [line.strip() for line in open('temps.txt')]
temperatures = [int(x) for x in temperatures]
i = 0
while i < len(temperatures):
    f.write(f"{9/5 * temperatures[i] + 32} \n")
    i = i +1
f.close()

input()

#---- ADDING NEW CONTENT TO FILES-----------
#This is called appending content. We use 'a' instead of 'w' in this case to append a new line to a
# file that already has some content

f = open('writefile.txt','a')
s = "This is line 3."
f.write(s)
f.close()

#f = open('writefile.txt','w')
#s = "This is line 4."
#f.write(s)
#f.close()
input()

#-----WRITING TO A FILE-------
#SAMPLE CODE
f = open('ftemps.txt','w')
temperatures = [line.strip() for line in open('temps.txt')]
temperatures = [int(x) for x in temperatures]
for t in temperatures:
    print(t*9/5 + 32, file=f)
f.close()

input()

f = open('writefile.txt','w')
print('This is line 1.',file = f)
print('This is line 2.',file = f)
f.close()

input()
#-------DIRECTORY LOCATIONS MATTER-----
s = open('C:/Users/sofia/OneDrive/Desktop/My Passwords.txt').read()
print(s)
input()

#----WAYS TO OPEN A FILE IN PYTHON-----
#Method 1
#The first way to read a text file uses a list comprehension to load the file line by line into a list.
#SAMPLE CODE
lines = [line.strip() for line in open('example.txt')]
print(lines)

#Method 2
#The second way of reading a text file loads the entire file into a string:
s = open('example.txt').read()
print(s)

