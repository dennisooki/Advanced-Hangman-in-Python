import json
import time
import random
with open('words.json') as f:
    words = json.load(f)

        

hangman_pics = {
    
    6: """
            x-------x
            |
            |
            |
            |
            |
        """,
    5: """
            x-------x
            |       |
            |       0
            |
            |
            |
        """,
    4: """
            x-------x
            |       |
            |       0
            |       |
            |
            |
        """,
    3: """
            x-------x
            |       |
            |       0
            |      /|\\
            |
            |
        """,
    2: """
            x-------x
            |       |
            |       0
            |      /|\\
            |      /
            |
        """,
    1: """
            x-------x
            |       |
            |       0
            |      /|\\
            |      / \\
            |
        """
}

def welcome():
    print('''     _       _                               _   _   _                                         
    / \   __| |_   ____ _ _ __   ___ ___  __| | | | | | __ _ _ __   __ _ _ __ ___   __ _ _ __  
   / _ \ / _` \ \ / / _` | '_ \ / __/ _ \/ _` | | |_| |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
  / ___ \ (_| |\ V / (_| | | | | (_|  __/ (_| | |  _  | (_| | | | | (_| | | | | | | (_| | | | |
 /_/   \_\__,_| \_/ \__,_|_| |_|\___\___|\__,_| |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                                                                   |___/                        \'''''')
    difficultySel()

def difficultySel():
  print("Select difficulty level:")  
  print("1.  EASY-Get hints without losing turns")
  print("2.  MEDIUM-Getting a hint reduces your turns by 1")
  print("3.  HARD-No hints")
  print("99. LEGACY-Just throws words at you, no context:LEGACY HANGMAN")
  difficulty=input()
  
  if difficulty == '1' or difficulty.upper()=='EASY':
    print('N00B difficulty selected')
    gameModeSel('EASY')

  elif difficulty=='2' or difficulty.upper()=='MEDIUM':
    print('MEDIUM difficulty selected')
    gameModeSel('MEDIUM')
    
  elif difficulty=='3'or difficulty.upper()=='HARD':
    print('Your bravery will be remembered soldier, entering HARD mode')
    gameModeSel('HARD')

  elif difficulty=='99'or difficulty.upper()=='LEGACY':
    print('Good to see you back Veteran, loading LEGACY mode')
    time.sleep(1)
    getWord('LEGACY','LEGACY')
    
  else:
    print('Invalid difficulty choice, try again')
    difficultySel()

def gameModeSel(diff):
  time.sleep(1)  
  print('Select game mode:')
  print('1.  Cities\n2.  Footballers\n3.  Famous People')   
  gamemode=input()
  
  if gamemode=='1'or gamemode.lower()=='cities':
    print("Launching CITIES mode in "+diff+' difficulty')
    getWord('CITIES',diff)

  elif gamemode=='2' or gamemode.lower()=='footballers':
    print("Launching FOOTBALLERS mode in "+diff+' difficulty')
    getWord('FOOTBALLERS',diff)

  elif gamemode=='3' or gamemode.lower()=='famous people':
    print("Launching Famous People mode in "+diff+' difficulty')
    getWord('THEFAMOUS',diff)

  else:
    print('Invalid game mode choice, try again')
    gameModeSel(diff)
 

def getWord(gmode,diff):
    prelist=[] 
    hintlist={}
    legacylist=[]
    if diff!='LEGACY':
        for i in words[gmode.lower()]:
            prelist.append(i)			#this loop gets the words 2 b guessed into a list        
        word2guess=random.choice(prelist)
        hintlist= words[gmode.lower()][word2guess]    #funnily enough hintlist is actually a dictionary
    
    else:
        for i in words:
            for j in words[i]:
                legacylist.append(j)
        word2guess=random.choice(legacylist)
    
    playGame(word2guess,diff,hintlist)
                     

def playGame(word2guess,diff,hintlist):
    turns = 6
    hints = 0
    # totalguess=''
    builtword=[]
    confirmword=[]
    for i in word2guess:
        confirmword.append(i+' ')
    
    for i in range(len(word2guess)):
    	builtword.append('_ ')
    print("Start guessing, type ? for hint")
    print(''.join(builtword))    
    print('\n')
    
    while turns>0 and confirmword!=builtword:
        
        currentguess=input()
        while not currentguess:
            print('Please give me something to work with:')
            currentguess=input()
            
        j=-1											#j keeps track of pstn in builtword list
        for i in word2guess:
            j+=1
            if i.lower()==currentguess[0].lower():		#solves the uppercase prblm in proper nouns and takes first str char
                builtword[j]=i+' '
                
        if currentguess=='?':
            if diff=='MEDIUM':
                  print(hangman_pics[turns])
            hints,turns=getHint(hints,diff,hintlist,turns) 	#impliment hint here
        	 

        elif currentguess.lower() not in word2guess.lower():
            print(hangman_pics[turns])
            turns-=1
        
        print('\n')
        if turns>6:
          turns=6        
        print(''.join(builtword))
        print('You have {} chances left'.format(turns))
        
    if confirmword==builtword:
        print("\nYou won with {} chances left and {} hints used".format(turns,hints))
        print('Type 1 to play again or any other key to quit da game')
        quit=input()
        if quit=='1':
            difficultySel()
        else:
            print('Ty 4 trying the game out <3')
    if turns==0:
        print("You lost, type 1 to play again or any other key to quit da game")
        quit=input()
        if quit=='1':
            difficultySel()
        else:
            print('Ty 4 trying the game out <3')
        
    
def getHint(hints,diff,hintlist,turns):
    if diff=='HARD' or diff=='LEGACY':
        print('NO HINTS IN {} DIFFICULTY'.format(diff))
        time.sleep(1)
        return hints,turns
    elif diff=='EASY' and hints!=len(hintlist):
        print(list(hintlist)[hints],':',hintlist[list(hintlist)[hints]])
        hints+=1
        return hints,turns
                           
    elif diff=='MEDIUM' and hints!=len(hintlist):
        print(list(hintlist)[hints],':',hintlist[list(hintlist)[hints]])
        hints+=1
        turns-=1
        return hints,turns

    else:
        print('NO MORE HINTS AVAILABLE')
        return hints,turns
    
    
          
welcome()
# hintlist= words['cities']
# print(hintlist)




