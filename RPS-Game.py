import random
import json
import sys



def getUsersFromDataBase(): #loads current dataBase to static userlist
 dataBaseFile = open('dataBase.json','r')
 
 userList = []
 
 for x in dataBaseFile.readlines():
  userList.append(json.loads(x))
  
 return userList
 
 
def saveThisUsersToDataBase(currentUserList): #save current userlist to dataBase file
 dataBaseFile = open('dataBase.json','w')
 
 serializedUserList = []
 
 for thisUser in currentUserList:
  serializedUserList.append(json.dumps(thisUser, default=lambda o: o.__dict__, 
            sort_keys=False, indent=1).replace("\n", "") + '\n')
  
 dataBaseFile.writelines(serializedUserList)


class user: #simple user objects

 @staticmethod
 def getUserList():
  userList = getUsersFromDataBase()
  return userList
 
 def __init__(this,name,user,password):
  this.name = name
  this.user = user
  this.password = password
  this.numberOfWins,this.numberOfLosses = 0,0
  
  
def getWins(this): #just return the numberOfWins field of users ---> used for comparator
 return this["numberOfWins"]
  
def showScores(userList): #prints score board
 userList.sort(reverse=True,key=getWins)
 print('\n                -=[SCORE BOARD]=- \n')
 
 for x in userList:
  print(" " + str(userList.index(x)+1) + ".  Player " + x["name"] + ' with ' + str(x["numberOfWins"]) + ' wins')

 
def checkExistenceOfUser(user,userList): # check an username is exists or not
 for x in userList:
  if x["user"] == user:
   return True
 
 return False

def showSignupMenu(): 
 inputtedUser = input('\n Please enter your username ... \n\n ')
 if checkExistenceOfUser(inputtedUser,user.getUserList()) == True :
  print('\n This username is already exists in our database. \n Please try again ...!')
 else :
  password = input('\n Please enter your password ... \n\n ')
  name = input('\n Please enter your name ... \n\n ')
  newUserList = user.getUserList()
  newUserList.append(user(name,inputtedUser,password))
  saveThisUsersToDataBase(newUserList)
  print('\n You are registered successfully ! \n Please try to login !')
  
  
def startNewGame(player):
 finalScore = int(input(' Enter game score limit\n '))
 
 playerScore,botScore = 0,0
 
 while (playerScore!=finalScore and botScore!=finalScore) :
  humanInput = input(' enter P for choose Paper, S as Scissor or R as Rock').upper()
  botChoice = random.choice(['P','S','R'])
  
  if (humanInput=='P' and botChoice=='P') or (humanInput=='S' and botChoice=='S') or (humanInput=='R' and botChoice=='R') :
   #Draw
   print('\n Draw ! \n Player : ' + str(playerScore) + '\n Bot : ' + str(botScore) + '\n')
  elif (humanInput=='P' and botChoice=='S') or (humanInput=='S' and botChoice=='R') or (humanInput=='R' and botChoice=='P'):
   #bot wins
   botScore = botScore+1
   print('\n Bot chose '+ str(botChoice) +' and took one point :( \n Player : ' + str(playerScore) + '\n Bot : ' + str(botScore) + '\n')
  elif (botChoice=='P' and humanInput=='S') or (botChoice=='S' and humanInput=='R') or (botChoice=='R' and humanInput=='P'):
   #player wins
   playerScore = playerScore+1
   print('\n Bot chose '+ str(botChoice) +' so you took one point :D \n Player : ' + str(playerScore) + '\n Bot : ' + str(botScore) + '\n')
   
 
 #taking the index of old player object 
 index = user.getUserList().index(player)
    

 if playerScore==finalScore :
  #Player won
  print(' \n You won this game :)')
  player["numberOfWins"] = player["numberOfWins"]+1
 else :
  #Bot won
  print(' \n You lost this game :(')
  player["numberOfLosses"] = player["numberOfLosses"]+1
  
 updatedPlayerList = user.getUserList()
 updatedPlayerList[index] = player
 
 saveThisUsersToDataBase(updatedPlayerList)
 
 showPanel(user.getUserList()[index])
  
 
 
  
def showPanel(thisUser):

 if thisUser["numberOfLosses"]+thisUser["numberOfWins"]==0:
  winRate = 0
 else : 
  winRate = thisUser["numberOfWins"]/(thisUser["numberOfLosses"]+thisUser["numberOfWins"])
  

 selection = input('\n                   +=[USER HOME PAGE]=+ \n User status : \n\n Number of your wins : '
 + str(thisUser["numberOfWins"]) + ' \n Number of your losses : ' + str(thisUser["numberOfLosses"]) +
 ' \n Your win rate : ' + str(winRate) + '\n\n=================================\n\n 1. Play a new game \n 2. Logout \n\n ')

 if selection == '1':
 
  #Start a new game
  startNewGame(thisUser)
  
  #when finished show user panel but not from here because we need to update players point
  
 elif selection == '2':
 
  #We called showMainMenu at the Outer scope, so we leave this case blank
  return
  
  
def showLoginMenu():

 inputtedUser = input('\n Please enter your username ...\n ')
 
 for x in user.getUserList():
  if x["user"] == inputtedUser:
   if input('\n Well, now please enter your password ...\n ') == x["password"]:
    showPanel(x)
    return
   else :
    print('\n Incorrect password !')
    return
   #break current for-loop and don't resume iterating on users
    
    
   
   
 print(' Not found in our dataBase :(')  


def showMainMenu():
 firstSelection = input('\n 1) Sign Up \n 2) Login \n 3) Score Board \n 4) Exit \n\n ')
 
 if firstSelection == '1':
 
  #Go to Sign Up menu
  showSignupMenu()
  
  #When finished show mainmenu
  showMainMenu()
  
 elif firstSelection == '2':
 
  #Go to login page
  showLoginMenu()
  
  #When finished show mainmenu
  showMainMenu()
  
 elif firstSelection == '3':
 
  #Show scoreboards
  showScores(user.getUserList())
  
  #When finished show mainmenu
  showMainMenu()
  
 elif firstSelection == '4':
 
  #Program force close
  sys.exit('\n Good luck :)')

#===================================================================================

#Run Game

user.getUserList() # for load users in start
showMainMenu()


