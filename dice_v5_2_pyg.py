#need 10000pts to win
#you can keep rolling for as long as you are getting pts
#you must score at least 1000pts in a turn in order to start recording your score
#if you roll again and wouldn't gain any more points, you lose all points from that turn

#move scoreKeeper section to outside of reRoll if statement
                #so it gives score so far before reroll
#add a point check to before asked to hold dice so you don't
                #have to choose held dice for a turn with no points
#have window popup and check boxes for holding dice

#I added detection for rolling three pairs but I disabled it for now to focus on other aspects

#maybe add: if savedScore > 10000, then savedScore -= (savedScore - 10000),
                #and print 'sorry fam, you need exactly 10000 to win'
                #either set score to 10000- how many points over 10000 it was
                # or set score to score - points gained this turn


#player 1 turn if turnCounter is odd, score saves to score1
#player 2 turn if turncounter is even, score saves to score2
#multiple players, create player class, playernum turnnum and once turnnum > max playernum, turnnum-maxplayernum=currplayernum

#TODO
#center the dice when there are less than 6
#add multiplayer suppport using arrays: put the whole damn thing in a for loop after the while loop
#to prep for multiplayer, move dice and text down by 50
#update heldscore up top whenever it changes

import random
from diceScoreIdea import scoreKeeper
import pygame
import time

clock = pygame.time.Clock()
pygame.init()
pygame.font.init()
black=[0,0,0]
white=[255,255,255]
green=[0,200,100]
red=[255,0,0]
blue=[0,50,255]

myfontBig = pygame.font.SysFont('Calibri', 30)
myfont = pygame.font.SysFont('Calibri', 20)
myfontSm = pygame.font.SysFont('Calibri', 15)



size = [640,480]
screen = pygame.display.set_mode(size)

def u(slp): #update display
    pygame.display.update()
    time.sleep(slp)
    
def refresh(slp): #clear screen
    screen.fill(black)
    u(slp)

anyKey = 'Press any key to continue...'

def getKP(xLoc,yLoc): #waits for user input to continue 220 280
    bullShitBool = False
    screen.blit((myfont.render(anyKey, False, white)),(xLoc,yLoc))
    u(0)
    while bullShitBool == False:
        clock.tick(10)
        pygame.event.clear()
        event = pygame.event.wait()
        if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:#later add mousepress
            bullShitBool = True
    screen.fill(black,(xLoc,yLoc,xLoc+180,yLoc+20))
    return bullShitBool

def getMP(yLoc): #for selecting held dice #give arg for location of buttons
    bullShitBool = False
    #yes
    pygame.draw.rect(screen,green,[(320-40-81),yLoc-3,81,31],2)#[199,347,81,31]
    screen.blit((myfontBig.render(('YES'),False,green)),((199+40-21),yLoc))
    #no
    pygame.draw.rect(screen,red,[(320+40),yLoc-3,81,31],2)#[360,347,81,31]
    screen.blit((myfontBig.render(('NO'),False,red)),(360+40-19,yLoc))
    u(0)
    while bullShitBool == False:
        clock.tick(10)
        mouseX, mouseY = pygame.mouse.get_pos()
        pygame.event.clear()
        event = pygame.event.wait()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if mouseX >= 199 and mouseX <= (199+81) and mouseY >= (yLoc-3) and mouseY <= (yLoc-3+31):#yes bounds
                yesButton = True
                noButton = False
                bullShitBool = True
            if mouseX >= 360 and mouseX <= (360+81) and mouseY >= (yLoc-3) and mouseY <= (yLoc-3+31):#no bounds
                yesButton = False
                noButton = True
                bullShitBool = True
    return yesButton, noButton
                
            
        
refresh(0)

pygame.display.set_caption("Dice Game v5")


holdDiceTurn = []#i reset the holdDiceArray after each turn because bug
diceArray=[]
newDiceArray=[]#temp array, will be set equal to diceArray for next roll
diceHeld=[0,0,0,0,0,0]#toggles
holdDiceArray=[]#dice actually held after roll
straightCounter = 0
rollCounter = 1
turnCounter = 1
tempScoreHeld = 0 #total score from held dice
setDice = [x for x in range (1,7)]
diceToRoll = 6#total dice - held dice
continueTurn = False
savedScore = 0
askHold = True #this is to skip the holding dice part if there are no points from the latest roll
#these booleans are for choosing held dice
yesButton = False
noButton = False 
playerCount = 0
#multiplayer arrays
numPlayer=[]
savedScorePlayer=[]
tempScoreHeldPlayer=[]
turnCounterPlayer=[]
rollCounterPlayer=[]


screen.blit((myfontBig.render('Welcome to Dice Game', False, white)),(180,220))
screen.blit((myfont.render('The goal of the game is to score 10,000 points', False, white)),(130,250))

u(0)

getKP(200,280)
refresh(0)
screen.blit((myfont.render('How many players?', False, white)),(140,100))

playerMax = 6
for i in range(playerMax):
    pygame.draw.rect(screen,white,[(70*i)+((640/2)-(35*playerMax)+10),150,50,50],2)
    pygame.draw.rect(screen,white,[(70*i)+((640/2)-(35*playerMax)+10),150,50,50],0)
    screen.blit((myfontBig.render((str(i+1)),False,black)),((70*i)+((640/2)-(35*playerMax)+30),160))
    u(0.25)

    
playerNumPicked = False
blueHigh = False
while playerNumPicked == False:
    clock.tick(60)
    mouseX, mouseY = pygame.mouse.get_pos()
    pygame.event.clear()
    event = pygame.event.wait()
    for i in range(playerMax):
        pygame.draw.rect(screen,white,[(70*i)+((640/2)-(35*playerMax)+10),150,50,50],2)
    if mouseY >= 150 and mouseY <= 200:
        for i in range(playerMax):
            if blueHigh == False:
                pygame.draw.rect(screen,white,[(70*i)+((640/2)-(35*playerMax)+10),150,50,50],2)
                xMin = (70*i)+((640/2)-(35*playerMax)+10)
                xMax = (70*i)+((640/2)-(35*playerMax)+10)+50
                yMin = 150
                yMax = 150+50
                clock.tick(60)
                mouseX, mouseY = pygame.mouse.get_pos()
                pygame.event.clear()
                event = pygame.event.wait()
                if mouseX >= xMin and mouseX <= xMax:
                    pygame.draw.rect(screen,blue,[xMin,150,50,50],2)
                    u(0)
                    blueHigh = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(playerMax):
                if playerNumPicked == False:
                    xMin = (70*i)+((640/2)-(35*playerMax)+10)
                    xMax = (70*i)+((640/2)-(35*playerMax)+10)+50
                    if mouseX >= xMin and mouseX <= xMax:
                        pygame.draw.rect(screen,green,[xMin,150,50,50],2)
                        u(0)
                        playerCount = i+1
                        playerNumPicked = True
    else:
        blueHigh = False

        
screen.blit((myfont.render('You selected '+str(playerCount)+' players.', False, white)),(140,240))

for i in range(playerCount): #create multiplayer arrays
    numPlayer.append(i+1)
    savedScorePlayer.append(0)
    tempScoreHeldPlayer.append(0)
    turnCounterPlayer.append(1)
    rollCounterPlayer.append(1)

                



continueTurn = getKP(200,280)
    

refresh(0)


while continueTurn == True:
    for player in range(playerCount):
        #fix so rerolls are dont change players
        #make sure only turncounter+1 changes player
        #while turncounter=x:all
        turnNum = turnCounterPlayer[player]
        while turnCounterPlayer[player] == turnNum:
            clock.tick(10)
            refresh(0)
            screen.blit((myfont.render(("Turn " + str(turnCounterPlayer[player]) + ", Roll " + str(rollCounterPlayer[player])),False,white)),(20,20))
            screen.blit((myfontSm.render(("Total Score: " + str(savedScorePlayer[player])),False,white)),(20,40))
            screen.blit((myfontSm.render(("Held Score: " + str(tempScoreHeldPlayer[player])),False,white)),(22,55))
            screen.blit((myfont.render("Player "+str(numPlayer[player]),False,white)),(320,20))
            u(0)
            #multiplayer scores
            for i in range(playerCount):
                screen.blit((myfontSm.render("Player "+str(numPlayer[i])+" Score: "+str(savedScorePlayer[i]),False,white)),(320,15*i+40))
            for i in range(diceToRoll):
                rollDice = random.randint(1,6)
                diceArray.append(rollDice)
                pygame.draw.rect(screen,white,[(70*i)+((640/2)-(35*diceToRoll)+10),150,50,50],2)
                pygame.draw.rect(screen,white,[(70*i)+((640/2)-(35*diceToRoll)+10),150,50,50],0)
                screen.blit((myfontBig.render((str(rollDice)),False,black)),((70*i)+((640/2)-(35*diceToRoll)+30),160))
                u(0.5)
            #diceArray.sort()
            
            ####################################################################

            quantDice = [diceArray.count(y) for y in setDice]
            tempScore = scoreKeeper(quantDice)
            
            if tempScore > 0:#zero check
                askHold = True
                            
            elif tempScore <= 0:
                askHold = False
            potScore = '(Potential '+str(tempScore)+'pts.)'
            screen.blit((myfontBig.render(potScore,False,white)),(200,220))
            u(1)
            getKP(200,280) #wait for input to continue

            ###########################################################################
            if askHold == True:
                tempDTR = diceToRoll #necessary due to inclusion of DTR var in calculations within for loop
                for i in range(diceToRoll):
                    #create center dice algorithm
                    pygame.draw.rect(screen,blue,[(70*i)+((640/2)-(35*diceToRoll)+10),150,50,50],4)
                    screen.blit((myfont.render(('Hold die?'),False,white)),(140,280))
                    u(0)
                    yesButton, noButton = getMP(320)#280 to 320
                    
                    if yesButton == True:
                        holdDiceArray.append(diceArray[i])
                        pygame.draw.rect(screen,green,[(70*i)+((640/2)-(35*diceToRoll)+10),150,50,50],4)
                        tempDTR -= 1
                        
                    elif noButton == True:
                        newDiceArray.append(diceArray[i])
                        pygame.draw.rect(screen,red,[(70*i)+((640/2)-(35*diceToRoll)+10),150,50,50],4)
                    u(0)
                diceToRoll = tempDTR
                screen.fill(black,(0,201,640,279)) #clear roll choices from screen    
                holdDiceTurn.append(holdDiceArray)
                quantDice = [holdDiceArray.count(y) for y in setDice]
                tempScore = scoreKeeper(quantDice)
               
                if tempScore > 0:#zero check
                    tempScoreHeldPlayer[player] += tempScore
                    screen.blit((myfont.render(('This roll, you have gained '+str(tempScore)+'pts.'),False,white)),(200,240))
                    screen.blit((myfont.render(('This turn, you have gained '+str(tempScoreHeldPlayer[player])+'pts.'),False,white)),(200,270))
                    screen.fill(black,(20,40,100,50))
                    screen.blit((myfontSm.render(("Total Score: " + str(savedScorePlayer[player])),False,white)),(20,40))
                    screen.blit((myfontSm.render(("Held Score: " + str(tempScoreHeldPlayer[player])),False,white)),(22,55))
                    u(0)
                    if diceToRoll > 0:
                        screen.blit((myfont.render(('You have '+str(diceToRoll)+' dice remaining.'),False,white)),(200,300))
                        screen.blit((myfont.render(('Reroll remaining dice?'),False,white)),(140,340))
                    if diceToRoll <= 0:
                        diceToRoll = 6
                        screen.blit((myfont.render(('You have used all of the dice.'),False,white)),(200,300))
                        screen.blit((myfont.render(('Reroll all dice to continue turn?'),False,white)),(140,340))
                    u(0)
                    yesButton, noButton = getMP(370)
                                        
                elif tempScore <= 0:
                    yesButton = False
                    noButton = True
                    tempScoreHeldPlayer[player] = 0
                    #getKP(200,280)
            
            elif askHold == False:
                yesButton = False
                noButton = True
                #tempScoreHeldPlayer[player] = 0
                getKP(200,280)
            
            diceArray = []
            newDiceArray = []
            screen.fill(black,(0,201,640,279))#clear all but the dice
            if yesButton == True and noButton == False: #reroll, continue turn
                rollCounterPlayer[player] += 1

             
            elif yesButton == False and noButton == True: #don't reroll, end turn
                rollCounterPlayer[player] = 1
                turnCounterPlayer[player] += 1
                diceToRoll = 6

                if tempScoreHeldPlayer[player] < 1000 and savedScorePlayer[player] <= 0:
                    savedScorePlayer[player] = 0
                    screen.blit((myfont.render(('No points gained this turn.'),False,white)),(200,250))
                    screen.blit((myfont.render(('You need at least 1000 points to advance'),False,white)),(140,280))

                elif tempScoreHeldPlayer[player] >= 1000 or savedScorePlayer[player] >= 1000:
                    savedScorePlayer[player] += tempScoreHeldPlayer[player]
                    screen.blit((myfont.render(('You gained '+str(tempScoreHeldPlayer[player])+'pts.'),False,white)),(200,280))
                    screen.fill(black,(20,40,100,50))
                    screen.blit((myfontSm.render(("Total Score: " + str(savedScorePlayer[player])),False,white)),(20,40))
                    screen.blit((myfontSm.render(("Held Score: " + str(tempScoreHeldPlayer[player])),False,white)),(22,55))
                u(0)
                holdDiceTurn = [] #reset held dice when turn ends 
                tempScoreHeldPlayer[player] = 0
            tempScore = 0
            holdDiceArray = [] #clears array so that next rolls score calc isnt affected
            if turnNum != turnCounterPlayer[player]:
                nextTurn = numPlayer[player]+1
                if nextTurn > playerCount:
                    nextTurn = 1
                screen.blit((myfont.render(("Begin Player "+str(nextTurn)+"'s Turn"),False,red)),(220,310))
                u(0)
            getKP(200,330)
            refresh(0)
        if savedScorePlayer[player] > 10000:
            savedScorePlayer[player] -= (savedScorePlayer[player]-10000)
        if savedScorePlayer[player] == 10000:
            screen.blit((myfontBig.render(('Winner: Player '+str(numPlayer[player])),False,white)),(200,250))
            continueTurn == False
            
        
