def scoreKeeper(quantVals):
    #global quantDice
    #global tempTempScore
    #global tempScore
    tempScore = 0
    
    if quantVals[0] == 1 or quantVals[0] == 2: #rolled one or two 1s
            tempTempScore = (100*quantVals[0])
            tempScore += tempTempScore

    if quantVals[4] == 1 or quantVals[4] == 2: #rolled one or two 5s 
            tempTempScore = (50*quantVals[4])
            tempScore += tempTempScore
                
    for i in range(6): #rolled three or more of a kind
            a = i+1
            if a == 1:
                    a = 10
            if quantVals[i] >= 3:
                    tempTempScore = (100*a*(2**(quantVals[i]-3)))
                    tempScore += tempTempScore
                        
    if quantVals == [1,1,1,1,1,1]: #rolled a straight
            tempScore += 1500

#        threePairs = quantVals #rolled three pairs
#        while 0 in threePairs:
#                threePairs.remove(0)
#        if threePairs == [2,2,2]: 
#                tempScore += 500

#    print ('(debug) tempScore in sK:',tempScore)                    
    return tempScore
