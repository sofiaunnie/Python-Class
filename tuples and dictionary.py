points={'A':1, 'B':3,'C':3, 'D':2, 'E':7,'F':4,'G':2,'H':4,'I':1,'J':8,
        'K':5,'L':9,'M':3,'N':5,'O':1,'P':3,'Q':10,'R':2,'S':8,'T':1,
        'U':3,'V':4,'W':4,'X':8,'Y':4,'Z':10}
p1_total_score=[]
p2_total_score=[]
print("-----------WORD GAME (SCRABBLE)-----------------")
print()
for i in range(3):
    print("-----------PLAYER 1 TURN-----------------")
    poneword = input('p1 Enter a word: ')
    poneword = poneword.upper()
    ponescore =sum([points[c] for c in poneword])
    print(ponescore)
    p1_total_score.append(ponescore)
    print("-----------PLAYER 2 TURN-----------------")
    p2word = input('p2 Enter a word: ')
    p2word = p2word.upper()
    p2score =sum([points[c] for c in p2word])
    print(p2score)
    p2_total_score.append(p2score)
print("-----------GAME OVER-----------------")
if p1_total_score > p2_total_score:
    print("PLAYER 1 WON")
elif p2_total_score > p1_total_score:
    print("PLAYER 2 WON")
else:
    print("IT'S A TIE")
print()
print("Player 1 total score is",sum(p1_total_score))
print("Player 2 total score is",sum(p2_total_score))
another_round = input("PLAY AGAIN? Y/N")
another_round.lower()



input()

points={'A':1, 'B':3,'C':3, 'D':2, 'E':7,'F':4,'G':2,'H':4,'I':1,'J':8,
        'K':5,'L':9,'M':3,'N':5,'O':1,'P':3,'Q':10,'R':2,'S':8,'T':1,
        'U':3,'V':4,'W':4,'X':8,'Y':4,'Z':10}

poneword = input('p1 Enter a word: ')
poneword = poneword.upper()
ponescore =sum([points[c] for c in poneword])
print(ponescore)
print("------------------------------")
p2word = input('p2 Enter a word: ')
p2word = p2word.upper()
p2score =sum([points[c] for c in p2word])
print(p2score)
input()
input()


animals= {'dog': 'has a tail and goes woof!',
          'cat': 'says meow',
          'mouse': 'chased by cats'}

word = input("Enter a word: ")
print('The definition is', animals[word])
input()

d={'A':100, 'B':200}


d['A']=400
print(d)

d['C']=500
print(d)


print(isinstance(d,dict))
print(type(d))
input()
days ={'January':31, 'February': 28, 'March':31, 'April':30, 'May':31,
       'June':30, 'July': 31, 'August':31, 'September':30, 'October':31,
       'November':30,'December':31}

print(days['January'])
print(days['December'])
print(days['November'])
input()

days = [31,28,31,30,31,30,31,31,30,31,30,31]

print(days[11])
print(days[-1])




input()

a=100
b=200

l = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
gaps_l = [l[i]-l[i-1] for i in range(1,len(l))]
print(gaps_l)
print("max gap size", max(gaps_l))
print(round((gaps_l.count(2)/len(gaps_l))*100,2))
#
# l = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
#
# newL = [(i-x) for i in l for x in l if l.index(x) + 1 == l.index(i)]
# print("", newL)
# print('max', max(newL))
# print('percentage',max(newL)/len(l)*100)

input()
# print(newL)

input()

l = [30,60,90]

indexes = [item[0] for item in enumerate(l)]
print(indexes)

input()

l = [30,60,90]
print(list(enumerate(l)))

input()
d = [1,2,3]
s = 'abcde'
t1=tuple(d)
t2 = tuple(s)

print(d)
print(s)
print(t1)
print(t2)

input()

new =("lawson","lanre")
print(type(new))


t = (1,2,3,-6)
# t.sort()
# print(t)
# t.reverse()
# print(t)

print(t[1:])
print(type(t))


l = [1,2,3,-6]
l.sort()
print(l)
l.reverse()
print(l)
