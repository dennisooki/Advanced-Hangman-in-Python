import json
import time

with open('words.json') as f:
  data = json.load(f)

for k in data:
  print(k)


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
    return difficulty

  elif difficulty=='2' or difficulty.upper()=='MEDIUM':
    print('MEDIUM difficulty selected')
    gameModeSel(difficulty)
    
  elif difficulty=='3'or difficulty.upper()=='HARD':
    print('Your bravery will be remembered soldier, entering HARD mode')
    return difficulty

  elif difficulty=='99'or difficulty.upper()=='LEGACY':
    print('Good to see you back Veteran, loading LEGACY mode')
    return difficulty
    
  else:
    print('Invalid difficulty choice, try again')
    difficultySel()

def gameModeSel(diff):
  print('Select game mode:')
  print('1.  Cities\n2.  Footballers\n3.  Famous People')
  gamemode=input()
  if gamemode=='1'or gamemode.lower()=='cities':
    print("Launching "+gamemode+' mode in'+diff+' difficulty')
  
welcome()
