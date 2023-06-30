#import pandas as pd


students = ['francis','faith','daniel','charles']
ages = [30,32,29,26]
RegNO = ['Sto1','Sto2','Sto3','Sto4']


# studtable =pd.DataFrame({
#     'Students': students,
#     'Ages':ages,
#     'Phone': ['Samsung', 'Huawei','Pixel','Xiaomi'],
#     'RegNO':RegNO
#})

# studtable.index = studtable.index + 1
studtable = studtable.set_index("RegNO")

print(studtable)
print("-----------")
print(studtable['Students'])
print("-----------")
print(studtable['Ages'])
print("-----------")
print(studtable['Students'][1])
print("-----------")
print(studtable['Ages'][1])
print("-----------")
print(studtable['Phone'])
print("-----------")
print(studtable['Phone'][3])

studtable.to_csv('Student Details.csv')
input()


teams = {'utah':3500,'warriors':3010,'nuggets':3880,'bulls':3900}
# add to a dictionary
teams['dolphins']=3750
print(teams)
print("----2----")
myteam= list(teams)
newteam =[teams[key]+10 for key in teams]
anotherTeam = {myteam[i]:newteam[i] for i in range(len(myteam))}

print(anotherTeam)
print("----3----")
teamlist = [x[0] for x in teams.items() if x[1] > 3600]
print(teamlist)

print("----4----")
for i in range(3):
    userTeam = input("Enter a Team: ").lower()
    userScore = eval(input("Enter a Score: "))
    teams[userTeam]=userScore #method 1
    # or
#     teams.update({userTeam: userScore}) #method 2
print(teams)
print("----5----")
updatedTeams =dict(sorted(teams.items(),key =lambda item:item[0]))
print(updatedTeams)

input()
months = {'January':31, 'February': 28, 'March':31, 'April':30, 'May':31,
       'June':30, 'July': 31, 'August':31, 'September':30, 'October':31,
       'November':30,'December':31}
print("---1---")
monthsName= input("Enter a Month: ").title()
print(months[monthsName])
print("---2---")
print(list(sorted(months)))
print("---3---")
monthlist = [x[0] for x in months.items() if x[1] == 31]
print(monthlist)
print("---4---")
monthsorted = dict(sorted(months.items(),key=lambda item:item[1]))
print(monthsorted)
input()


d={'thor':41,'zeus':70,'hela':90,'strange':22,'xzavier':57,'loki':45}
dsorted = dict(sorted(d.items(),key=lambda item:item[0]))

dsorted2 = dict(sorted(d.items(),key=lambda item:item[1]))

print(dsorted)
print(dsorted2)
input()
students = ['francis','faith','daniel','charles']
ages = [30,32,29,26]
studetails = dict(zip(students,ages))
studetails2 = list(zip(students,ages))
# print(studetails)
# print(studetails2)

studetails3 ={students[i]:ages[i] for i in range( len(students))}
print(studetails3)
input()
dstars={'thor':41,'zeus':70,'hela':41,'strange':22,'xavier':57,'loki':45}
x=[item[1] for item in dstars.items()]
print(x)

input()
letters ={'A':100,'B':200, 'C':100,'D':300}
keys_100 = [x[0] for x in letters.items() if x[1] ==100]
print(keys_100)

dstars={'thor':41,'zeus':70,'hela':41,'strange':22,'xavier':57,'loki':45}
ditemsrev =[(x[1],x[0]) for x in dstars.items()]

print(ditemsrev)
input()

alpha = ["a","b","c","d","e","f"]
print(list(enumerate(alpha)))
print(dict(enumerate(alpha)))


teams = {'man city':86, 'liverpool':83,'chelsea':67, 'arsenal':66, 'spurs':62}
print("-------A-------")
print(sum([teams[key] for key in teams]))
print("-------B-------")
print(sum(list(teams.values())))
print("-------C-------")
print(sum([key[1] for key in teams.items()]))
input()


total =0
for i in range(len(teams)):
    user = input("Enter a team: ").lower()
    print("Team Points: ", teams[user])
    total = total + teams[user]
    print(total)
input()




dstars={'thor':41,'zeus':70,'hela':41,'strange':22,'xavier':57,'loki':45}
x=[item[1] for item in dstars.items()]
print(x)

input()
letters ={'A':100,'B':200, 'C':100,'D':300}
keys_100 = [x[0] for x in letters.items() if x[1] ==100]
print(keys_100)

dstars={'thor':41,'zeus':70,'hela':41,'strange':22,'xavier':57,'loki':45}
ditemsrev =[(x[1],x[0]) for x in dstars.items()]

print(ditemsrev)
input()
l = [6,7,8,9]
l.reverse()
print(l)


input()

dstars={'thor':41,'zeus':70,'hela':41,'strange':22,'xavier':57,'loki':45}

print(list(dstars))
print([dstars[keys] for keys in dstars] == list(dstars.values()))
print(list(dstars.items()))

input()
keys = [key[::-1]  for key in dstars]
print(keys)



input()
d = {'A':1,'B':3}
print(list(d))
print(d.values())
print(d.items())

input()

alphabets =[('A',[40,50]),('B',[60,70])]
dictalpha = dict(alphabets)
print(dictalpha)


ans = [dictalpha[keys] for keys in dictalpha]
print(ans)




input()
d={'thor':41,'zeus':70,'hela':41,'strange':22,'xzavier':57,'loki':45}

dvals = [d[keys] for keys in d]
print(dvals)

for key in d:
    print(d[key])
input()
keys = [key for key in d]
print(keys)

input()
# looping through the dictionary keys
for key in d:
    print(key)
# --------
if "THOR" in d:
    print(d["THOR"])