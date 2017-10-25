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

import random
from diceScoreIdea import scoreKeeper
from tkinter import *
import time




holdDiceTurn = []#i reset the holdDiceArray after each turn because bug
diceArray=[]
newDiceArray=[]#temp array, will be set equal to diceArray for next roll
diceHeld=[0,0,0,0,0,0]#toggles
holdDiceArray=[]#dice actually held after roll
straightCounter = 0
rollCounter = 1
turnCounter = 1
#tempScore = 0 #over max possible score for roll (just checked for nonzero value)
tempScoreHeld = 0 #total score from held dice
setDice = [x for x in range (1,7)]
diceToRoll = 6#total dice - held dice
continueTurn = False
savedScore = 0
rRoll = '' #input asking if you want to reroll non-held dice
askHold = True #this is to skip the holding dice part if there are no points from the latest roll
debugMode = False #precede all debugs with if debugMode == True:
#threePairs = [] #used for score detection of three pairs


#continueTurn = True


gameBox = Tk()
gameBox.title('Dice Game')
gameBox.geometry('300x300')


#app = Frame(gameBox)
#app.grid()
#exitButton = Button(app,text = 'Exit',width=2,command=exit)
#exitButton.grid(padx=110,pady=80)
def conTurn():
    #input('input')
    global continueTurn
    continueTurn = True
    print('Within function:',continueTurn)
    welcomeText.destroy()
    rulesText.destroy()
    startButton.destroy()
    print("destroyed sB")
    #gameBox.destroy() #I'm in process of putting all in gui
        

#print('Welcome to Dice Game')
#print('The goal of the game is to score 10,000 points in the shortest number of turns')
#print ('')
#print(':::::::::::::::::::::::::::::::::::::::::::::::::')
welcomeText = Message(gameBox,width=150,text="Welcome to Dice Game")
welcomeText.pack()
rulesText = Message(gameBox,width=200,text="Your goal is to score 10,000 points in the shortest number of turns")
rulesText.pack()
startButton = Button(gameBox, text="Start",command=conTurn)
startButton.pack()

print("before sB loop end")

#while continueTurn == False: #this is laggy as hell
startButton.update_idletasks()
startButton.update()
#i want the program to wait until the start button is pressed to continue

print("ended sB",continueTurn)


while continueTurn == True:
    print("entered while loop")
    turn1 = "Turn " + str(turnCounter) + ", Roll " + str(rollCounter)
    turn2 = "Total Score: " + str(savedScore)
    turn3 = "Score This Turn: " + str(tempScoreHeld)
    turnText = Message(gameBox,width=200,text=turn1)
    turnText.pack()
    print("after turntext")
    input()#wait for input to continue
    print ('')
    print (turn1)
    print ("    ",turn2)
    print ("    ",turn3)
    print (':::::::::::::::::::::::::::::::::::::::::::::::::')
    for i in range(diceToRoll):
        rollDice = random.randint(1,6)
        diceArray.append(rollDice)
    diceArray.sort()
    print ('Your Roll: ',diceArray)
    

    ####################################################################

    quantDice = [diceArray.count(y) for y in setDice]
    
    tempScore = scoreKeeper(quantDice)
    if debugMode == True: print ('(debug) tempScore:',tempScore)               

    if tempScore > 0:#zero check
        askHold = True
                    
    elif tempScore <= 0:
        askHold = False
           
    print ('Potential',tempScore,'pts.')       
    #tempScore = 0
    ###########################################################################

    if askHold == True:
        print ('Dice: ',diceArray)
        for i in range(diceToRoll):
            print ('Hold die ',setDice[i],'? (',diceArray[i],')')
            tempX = int(input())#enter 1 for hold, other for reroll
            diceHeld[i] = tempX
        print ('Dice: ',diceArray)
        if debugMode == True: print ('(debug) diceHeldToggles: ',diceHeld)

        for i in range(diceToRoll):
            if diceHeld[i] == 1:
                holdDiceArray.append(diceArray[i])
                diceToRoll -= 1
            elif diceHeld[i] != 1:
                newDiceArray.append(diceArray[i])
                        
        print('Held Dice: ',holdDiceArray)
        holdDiceTurn.append(holdDiceArray)
        if debugMode == True: print('(debug) holdDiceTurn:',holdDiceTurn)
        if debugMode == True: print('(debug) Dice to Reroll:',newDiceArray)
        if debugMode == True: print('(debug) diceToRoll:',diceToRoll)

        #score calculations because i can't figure out def
        quantDice = [holdDiceArray.count(y) for y in setDice]
        if debugMode == True: print ('(debug) quantDice: ',quantDice)
        tempScore = scoreKeeper(quantDice)
                
        if tempScore > 0:#zero check
            tempScoreHeld += tempScore
            print ('This roll, you have gained',tempScore,'pts.')
            print ('This turn, you have gained',tempScoreHeld,'pts.')
            if diceToRoll > 0:
                print ('You have',diceToRoll,'dice remaining.')
                rRoll = input('Reroll remaining dice? ')
            if diceToRoll <= 0:
                diceToRoll = 6
                print ('You have used all of the dice.')
                rRoll = input('Reroll all dice to continue turn? ')
                                
        elif tempScore <= 0:
           if debugMode == True: print ('(debug)',tempScore,'pts')
           if debugMode == True: print('(debug) no pts from your roll. 0pts gained this turn. begin next turn.')
           rRoll = 'no'
           tempScoreHeld = 0
    
    elif askHold == False:
        rRoll = 'no'
        tempScoreHeld = 0
    

    diceArray = []
    newDiceArray = []
    if rRoll == 'yes':
        rollCounter += 1

            
    elif rRoll != 'yes':
        rollCounter = 1
        turnCounter += 1
        diceToRoll = 6
        if tempScoreHeld < 1000 and savedScore <= 0:
            savedScore = 0
            print ('No points gained.')
        elif tempScoreHeld >= 1000 or savedScore >= 1000:
            savedScore += tempScoreHeld
            print ('You gained',tempScoreHeld,'pts.')
        
        holdDiceTurn = [] #reset held dice when turn ends 
        tempScoreHeld = 0
    tempScore = 0
    holdDiceArray = [] #clears array so that next rolls score calc isnt affected
    print ('')
    input('Press Enter to continue...')
    print ('')
    turnText.destroy()


#print('After while loop:',continueTurn)

gameBox.mainloop()







        
