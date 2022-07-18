import json
import time
import random
with open('words.json') as f:
    words = json.load(f)

        


def welcome():
  print("Welcome Enter your name:")
  player=input()
  print("Hi "+player+". Select difficulty level:")
  time.sleep(1)
  difficultySel()

def difficultySel():
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
    return 0
    
  else:
    print('Invalid difficulty choice, try again')
    difficultySel()

def gameModeSel(diff):
  time.sleep(1.5)  
  print('Select game mode:')
  print('1.  Cities\n2.  Footballers\n3.  Famous People')   #change these to \t
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
    hintlist=[]
    for i in words[gmode.lower()]:
        prelist.append(i)			#this loop gets the words 2 b guessed into a list        
    
    word2guess=random.choice(prelist)
    for i,j in words[gmode.lower()][word2guess].items():
    	hintlist.append(j)
           
    playGame(word2guess,diff,hintlist)
    
        

          


def playGame(word2guess,diff,hintlist):
    turns = 10
    hints = 3
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
        j=-1											#j keeps track of pstn in builtword list
        for i in word2guess:
            j+=1
            if i.lower()==currentguess[0].lower():		#solves the uppercase prblm in proper nouns and takes first str char
                builtword[j]=i+' '
                
        if currentguess=='?':
        	hints,turns=getHint(hints,diff,hintlist,turns) 	#impliment hint here
        
        if currentguess.lower() not in word2guess.lower():
            turns-=1
        
        print('\n')
        if turns>10:
          turns=10        
        print(''.join(builtword))
        print('You have {} chances left'.format(turns))
        
    if confirmword==builtword:
        print("\nYou won with {} chances and {} hints left".format(turns,hints))
    
    
    
    
def getHint(hints,diff,hintlist,turns):
    if diff=='HARD' or diff=='LEGACY':
        print('NO HINTS IN {} DIFFICULTY'.format(diff))
        time.sleep(1)
        turns+=1
        return hints,turns
    elif diff=='EASY':
        if hints==3:
            print(hintlist[0])
            hints-=1
            turns+=1
            return hints,turns
             
        elif hints==2:
            print(hintlist[1])
            hints-=1
            turns+=1
            return hints,turns
            
        elif hints==1:
            print(hintlist[2])
            hints-=1
            turns+=1
            return hints,turns
             
            
    elif diff=='MEDIUM':
        if hints==3:
            print(hintlist[0])
            hints-=1
            return hints,turns
             
        elif hints==2:
            print(hintlist[1])
            hints-=1
            return hints,turns
            
        elif hints==1:
            print(hintlist[2])
            hints-=1
            return hints,turns
        elif hints==0:
            print('NO MORE HINTS AVAILABLE')
            turns+=1
            return hints,turns
    
    
    

# getWord('FOOTBALLERS','LEGACY')  
# playGame('Ronaldo',2)        
welcome()




