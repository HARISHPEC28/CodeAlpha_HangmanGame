import random
l=["apple", "banana", "orange", "mango", "grapes", "pineapple", "watermelon", "kiwi", "papaya", "strawberry"]

word=l[random.randint(0,3)]
lives=6
stages = [
    """
  _______
 |       |
 |
 |
 |
_|_
""",
    """
  _______
 |       |
 |       O
 |
 |
_|_
""",
    """
  _______
 |       |
 |       O
 |       |
 |
_|_
""",
    """
  _______
 |       |
 |       O
 |      /|
 |
_|_
""",
    """
  _______
 |       |
 |       O
 |      /|\\
 |
_|_
""",
    """
  _______
 |       |
 |       O
 |      /|\\
 |      /
_|_
""",
    """
  _______
 |       |
 |       O
 |      /|\\
 |      / \\
_|_
"""
]


print("!!!!!!!!!!!HANGMAN GAME!!!!!!!!!!!")
print("guess the fruit name")
print("total lives",lives)


wl=[] #WORD AS LIST
for i in range(len(word)):
    wl.append('_')
print(wl)
temp=list(word)
ctemp=[]

for i in temp:
    ctemp.append(i)
print(stages[0])
s=0





while(lives>=1):
    guess=input("enter your guess: ")
    if not guess.isalpha():
        print("enter a letter!!!")
        continue
    elif len(guess)>1:
        print("enter only one letter!!!")
        continue
    else:
        guess=guess.lower()
    if (guess in ctemp):
        wl[ctemp.index(guess)]=guess
        ctemp[ctemp.index(guess)]="'-'"
        print(stages[s])
        print("correct guess")
        print(wl)
        temp.remove(guess)
        
        
        if(len(temp)==0):
            print("!!!!!!!!!!!!!!YOU WON!!!!!!!!!!MAN SAVED!!!!!!!!!!")
            break
    else:
        print("wrong gusse")
        lives-=1
        s+=1
        
        print(stages[s])
        print(wl)
        
else:
    print("!!!!!!!!!!!YOU LOST!!!!!!!!!!!!!!!!MAN HANGED!!!!!!!!!!!!!!! ")

