# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 14:54:28 2020
Steroid KNN

@author: Noah
"""

global inFile
inFile = open('C:/Users/Noah/champdataverbose.txt', 'r')
    
#gets data for the user champion from the champion list
def retrieve_userChamp_data(_USERCHAMP, inFile):
    with inFile as currFile:
        line = currFile.readline()
        for line in currFile:
            if _USERCHAMP in line:
                return line
    
    
def compute_similarity_scores(inFile, _USERLINE, stat):
    inFile = open('C:/Users/Noah/champdataverbose.txt', 'r')
    out = []
    dict = {'Lane':0, 'Role':1, 'Damage':2, 'HardCC':3, 'HardEngage':4, 'Disengage':5, 'Poke':6, 'Waveclear':7, 'Tank':8, 
            'Mobility':9, 'Scaling':10, 'Snowball':11, 'Burst':12, 'Game':13, 'Difficulty':14, 'Manaless':15}
    givenStat = dict.get(stat)
    with inFile as currFile:
        line = currFile.readline()
        for line in currFile:
            
            #create a line list of the input champion
            _USERLINElist = _USERLINE.split(',')
            _USERLINElist.pop(0)
            
            #create line list of current line in file
            attributeTemp = line.split(',')
            
            #remove champion name and store in a temp variable
            champName = attributeTemp[0]
            attributeTemp.pop(0)
            outScore = float(0)
            
            #if the current line list is not the userline
            if(attributeTemp != _USERLINElist):
                
                #manaless is important at 1.5
                if(attributeTemp[15] == _USERLINElist[15]):
                    outScore += 1.5
                    #steroid for manaless
                    if givenStat == 15:
                        outScore += 10
                    attributeTemp.pop(15)
                    _USERLINElist.pop(15)
                    
                    
                #difficulty important at 2.0
                if(attributeTemp[14] == _USERLINElist[14]):
                    outScore += 2.0
                    #steroid for difficulty
                    if givenStat == 14:
                        outScore += 10
                    attributeTemp.pop(14)
                    _USERLINElist.pop(14)
                    
                
                #make sure game is an important score at +1.75
                if(attributeTemp[13] == _USERLINElist[13]):
                    outScore += 1.75
                    #steroid for game
                    if givenStat == 13:
                        outScore += 10
                    attributeTemp.pop(13)
                    _USERLINElist.pop(13)
                    
                    
                
                #steroid for burst
                if((attributeTemp[12] == _USERLINElist[12]) and givenStat == 12):
                    outScore += 10
                    
                #steroid for snowball
                if((attributeTemp[11] == _USERLINElist[11]) and givenStat == 11):
                    outScore += 10
                    
                #steroid for scaling
                if((attributeTemp[10] == _USERLINElist[10]) and givenStat == 10):
                    outScore += 10
                
                #steroid for mobility
                if((attributeTemp[9] == _USERLINElist[9]) and givenStat == 9):
                    outScore += 10
                
                #steroid for tank
                if((attributeTemp[8] == _USERLINElist[8]) and givenStat == 8):
                    outScore += 10
                
                #create a 0.5 value for Poke and Waveclear if they are both true and flipped
                if((attributeTemp[6] and _USERLINElist[7] == '1') or (_USERLINElist[6] and attributeTemp[7] == '1')):
                    outScore += 0.5
                    #steroid for waveclear
                    if((attributeTemp[7] == _USERLINElist[7]) and givenStat == 7):
                        outScore += 10
                    #steroid for poke
                    if((attributeTemp[6] == _USERLINElist[6]) and givenStat == 6):
                        outScore += 10
                    attributeTemp.pop(6)
                    attributeTemp.pop(7)
                    _USERLINElist.pop(6)
                    _USERLINElist.pop(7)
                
                #steroid for disengage
                if((attributeTemp[5] == _USERLINElist[5]) and givenStat == 5):
                    outScore += 10  
                    
                #create a 0.5 value for HardCC and HardEngage if they are both true and flipped
                if((attributeTemp[3] and _USERLINElist[4] == '1') or (attributeTemp[4] and _USERLINElist[3] == '1')):
                    outScore += 0.5
                    #steroid for HardEngage
                    if((attributeTemp[4] == _USERLINElist[4]) and givenStat == 4):
                        outScore += 10
                    #steroid for HardCC
                    if((attributeTemp[3] == _USERLINElist[3]) and givenStat == 3):
                        outScore += 10
                    attributeTemp.pop(3)
                    attributeTemp.pop(4)
                    _USERLINElist.pop(3)
                    _USERLINElist.pop(4)
                
                #steroid for Damage
                if((attributeTemp[2] == _USERLINElist[2]) and givenStat == 2):
                    outScore += 10
                
                #make sure archetype is another important score at +1.5
                if(attributeTemp[1] == _USERLINElist[1]):
                    outScore += 1.5
                    #steroid for role
                    if givenStat == 1:
                        outScore += 10
                    attributeTemp.pop(1)
                    _USERLINElist.pop(1)
                    
                #make sure lane is the most important score at +3
                if(attributeTemp[0] == _USERLINElist[0]):
                    outScore += 1
                    #steroid for lane
                    if givenStat == 0:
                        outScore += 10
                    attributeTemp.pop(0)
                    _USERLINElist.pop(0)
                
                
                
                #check for identical elements at the same indeces, if they are
                #identical, add a 1 to the final score
                for i in range(len(attributeTemp)):
                    if _USERLINElist[i] == attributeTemp[i]:
                        outScore += 1.0
                out.append(champName)
                out.append(float(outScore))
               
    return out

def compute_similarity_scores_BASELINE(inFile, _USERLINE, stat):
    inFile = open('C:/Users/Noah/champdataverbose.txt', 'r')
    out = []
    dict = {'Lane':0, 'Role':1, 'Damage':2, 'HardCC':3, 'HardEngage':4, 'Disengage':5, 'Poke':6, 'Waveclear':7, 'Tank':8, 
            'Mobility':9, 'Scaling':10, 'Snowball':11, 'Burst':12, 'Game':13, 'Difficulty':14, 'Manaless':15}
    givenStat = dict.get(stat)
    with inFile as currFile:
        line = currFile.readline()
        for line in currFile:
            
            #create a line list of the input champion
            _USERLINElist = _USERLINE.split(',')
            _USERLINElist.pop(0)
            
            #create line list of current line in file
            attributeTemp = line.split(',')
            
            #remove champion name and store in a temp variable
            champName = attributeTemp[0]
            attributeTemp.pop(0)
            outScore = float(0)
            
            #if the current line list is not the userline
            if(attributeTemp != _USERLINElist):
                
                #steroid for manaless
                if((attributeTemp[15] == _USERLINElist[15]) and givenStat == 15):
                    outScore += 10
                attributeTemp.pop(15)
                _USERLINElist.pop(15)
                    
                    
                #steroid for difficulty
                if((attributeTemp[14] == _USERLINElist[14]) and givenStat == 14):
                    outScore += 10
                attributeTemp.pop(14)
                _USERLINElist.pop(14)
                    
                #steroid for game
                if((attributeTemp[13] == _USERLINElist[13]) and givenStat == 13):
                    outScore += 10
                attributeTemp.pop(13)
                _USERLINElist.pop(13)
                    
                #steroid for burst
                if((attributeTemp[12] == _USERLINElist[12]) and givenStat == 12):
                    outScore += 10
                    
                #steroid for snowball
                if((attributeTemp[11] == _USERLINElist[11]) and givenStat == 11):
                    outScore += 10
                    
                #steroid for scaling
                if((attributeTemp[10] == _USERLINElist[10]) and givenStat == 10):
                    outScore += 10
                
                #steroid for mobility
                if((attributeTemp[9] == _USERLINElist[9]) and givenStat == 9):
                    outScore += 10
                
                #steroid for tank
                if((attributeTemp[8] == _USERLINElist[8]) and givenStat == 8):
                    outScore += 10
                    attributeTemp.pop(8)
                    _USERLINElist.pop(8)
                
                #steroid for waveclear
                if((attributeTemp[7] == _USERLINElist[7]) and givenStat == 7):
                    outScore += 10
                    attributeTemp.pop(7)
                    _USERLINElist.pop(7)
                    
                #steroid for poke
                if((attributeTemp[6] == _USERLINElist[6]) and givenStat == 6):
                    outScore += 10
                    attributeTemp.pop(6)
                    _USERLINElist.pop(6)
                
                
                #steroid for disengage
                if((attributeTemp[5] == _USERLINElist[5]) and givenStat == 5):
                    outScore += 10
                    _USERLINElist.pop(5)
                    attributeTemp.pop(5)
                    
                #steroid for HardEngage
                if((attributeTemp[4] == _USERLINElist[4]) and givenStat == 4):
                    outScore += 10
                    attributeTemp.pop(4)
                    _USERLINElist.pop(4)
                    
                #steroid for HardCC
                if((attributeTemp[3] == _USERLINElist[3]) and givenStat == 3):
                    outScore += 10
                    attributeTemp.pop(3)
                    _USERLINElist.pop(3)
                    
                
                #steroid for Damage
                if((attributeTemp[2] == _USERLINElist[2]) and givenStat == 2):
                    outScore += 10
                
                #steroid for role
                if((attributeTemp[1] == _USERLINElist[1]) and givenStat == 1):
                    outScore += 10
                    attributeTemp.pop(1)
                    _USERLINElist.pop(1)
                    
                #steroid for lane
                if((attributeTemp[0] == _USERLINElist[0]) and givenStat == 0):
                    outScore += 10
                    attributeTemp.pop(0)
                    _USERLINElist.pop(0)
                
                
                
                #check for identical elements at the same indeces, if they are
                #identical, add a 1 to the final score
                for i in range(len(attributeTemp)):
                    if _USERLINElist[i] == attributeTemp[i]:
                        outScore += 1.0
                out.append(champName)
                out.append(float(outScore))
               
    return out
    
def organize_output_list(out):
    #two lists for output purposes
    champNames = []
    champScores = []
    for obj in out:
        #if the element is a string, it is a name; add it to champNames list
        if(isinstance(obj, str)):
            champNames.append(obj)
        else:
            #if it's a float, it's a score; add it to champScores list
            champScores.append(float(obj))
    #grab largest score from champScores
    largestScoreIndex = champScores.index(max(champScores))
    #parallel the index in champScores to champNames since they are organized in the same way
    return print("The champion you would most likely also enjoy based on your input is " + champNames[largestScoreIndex])


def organize_output_list_SHORT(out):
    #2 lists for organized output
    champNames = []
    champScores = []
    for obj in out:
        if(isinstance(obj, str)):
            champNames.append(obj)
        else:
            champScores.append(int(obj))
    largestScoreIndex = champScores.index(max(champScores))
    return print(champNames[largestScoreIndex])


def organize_output_list_FIVE(out):
    champNames = []
    champScores = []
    outScores =[]
    outIndexes = []
    outFinal = []
    for obj in out:
        if(isinstance(obj, str)):
            champNames.append(obj)
        else:
            champScores.append(float(obj))
    for i in range(0, 5):  
        max1 = float(0)
        maxIndex = 0
        for j in range(len(champScores)):      
            if champScores[j] > max1: 
                max1 = champScores[j];
                maxIndex = j
        champScores.remove(max1) 
        outScores.append(maxIndex)
        outIndexes.append(maxIndex)
    for score in outScores:
        outFinal.append(champNames[score])
        champNames.remove(champNames[score])
    return outFinal


def generate_nameList():
    inFile = open('C:/Users/Noah/champdataverbose.txt', 'r')
    nameList = []
    with inFile as currFile:
        line = currFile.readline()
        for line in currFile:
            temp = line.split(',')
            name = temp[0]
            nameList.append(name)
    return nameList
     
           
def main():
    attributeList = ["HardCC", "HardEngage", "Disengage", "Poke", "Waveclear", "Tank", "Mobility", "Scaling", "Snowball", 
                     "Burst", "Game", "Difficulty", "Manaless"]
    inFile = open('C:/Users/Noah/champdataverbose.txt', 'r')
    stat = "Snowball"
    #single input - from command line
    #print("Please enter a champion: ")
    #_USERCHAMP = input("")
    _USERCHAMP = "Amumu"
    for string in attributeList:
        inFile = open('C:/Users/Noah/champdataverbose.txt', 'r')
        #print("-------------FOR ATTRIBUTE: ", string, "---------------")
        _USERLINE = retrieve_userChamp_data(_USERCHAMP, inFile)
        outList = compute_similarity_scores_BASELINE(inFile, _USERLINE, string)
        print("For Champion: ", _USERCHAMP, ", and stat: ", string)
        print(organize_output_list_FIVE(outList))
        print("\n")
    #print(outList)
    """
    #un-comment next block for analysis on every champion rather than one only
    
    #every champion
    print("EVERY CHAMPION: ")
    champList = generate_nameList()
    for i in range(len(champList)):
        inFile = open('C:/Users/Noah/champdataverbose.txt', 'r')
        _USERCHAMP = champList[i]
        _USERLINE = retrieve_userChamp_data(_USERCHAMP, inFile)
        outList = compute_similarity_scores(inFile, _USERLINE, stat)
        print("For the champion: ", _USERCHAMP)
        organize_output_list_SHORT(outList)
    
    #every champ per steroided stat
    champList = generate_nameList()
    attributeList = ["HardCC", "HardEngage", "Disengage", "Poke", "Waveclear", "Tank", "Mobility", "Scaling", "Snowball", 
                     "Burst", "Game", "Difficulty", "Manaless"]
    for string in attributeList:
        print("-------------FOR ATTRIBUTE: ", string, "---------------")
        for i in range(len(champList)):
            inFile = open('C:/Users/Noah/champdataverbose.txt', 'r')
            _USERCHAMP = champList[i]
            _USERLINE = retrieve_userChamp_data(_USERCHAMP, inFile)
            outList = compute_similarity_scores(inFile, _USERLINE, string)
            print("For the champion: ", _USERCHAMP)
            print(organize_output_list_FIVE(outList))
    """
    #housekeeping
    inFile.close()
   
if __name__ == '__main__':
    main()