# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 11:11:11 2020
Second build of champion similarity, uses Euclidean distance rather than SequenceMatcher
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
    
    
def compute_similarity_scores(inFile, _USERLINE):
    inFile = open('C:/Users/Noah/champdataverbose.txt', 'r')
    out = []
    
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
                    attributeTemp.pop(15)
                    _USERLINElist.pop(15)
                    
                #difficulty important at 2.0
                if(attributeTemp[14] == _USERLINElist[14]):
                    outScore += 2.0
                    attributeTemp.pop(14)
                    _USERLINElist.pop(14)
                
                #make sure game is an important score at +1.75
                if(attributeTemp[13] == _USERLINElist[13]):
                    outScore += 1.75
                    attributeTemp.pop(13)
                    _USERLINElist.pop(13)
                
                #create a 0.5 value for Poke and Waveclear if they are both true and flipped
                if((attributeTemp[6] and _USERLINElist[7] == '1') or (_USERLINElist[6] and attributeTemp[7] == '1')):
                    outScore += 0.5
                    attributeTemp.pop(6)
                    attributeTemp.pop(7)
                    _USERLINElist.pop(6)
                    _USERLINElist.pop(7)
                    
                #create a 0.5 value for HardCC and HardEngage if they are both true and flipped
                if((attributeTemp[3] and _USERLINElist[4] == '1') or (attributeTemp[4] and _USERLINElist[3] == '1')):
                    outScore += 0.5
                    attributeTemp.pop(3)
                    attributeTemp.pop(4)
                    _USERLINElist.pop(3)
                    _USERLINElist.pop(4)
                
                #make sure archetype is another important score at +1.5
                if(attributeTemp[1] == _USERLINElist[1]):
                    outScore += 1.5
                    attributeTemp.pop(1)
                    _USERLINElist.pop(1)
                    
                #make sure lane is the most important score at +2
                if(attributeTemp[0] == _USERLINElist[0]):
                    outScore += 2
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
    inFile = open('C:/Users/Noah/champdataverbose.txt', 'r')
    
    #single input
    print("Please enter a champion: ")
    _USERCHAMP = input("")
    _USERLINE = retrieve_userChamp_data(_USERCHAMP, inFile)
    outList = compute_similarity_scores(inFile, _USERLINE)
    print(organize_output_list(outList))
    #print(outList)
    
    #un-comment next block for analysis on every champion rather than one only
    
    #every champion
    print("EVERY CHAMPION: ")
    champList = generate_nameList()
    for i in range(len(champList)):
        inFile = open('C:/Users/Noah/champdataverbose.txt', 'r')
        _USERCHAMP = champList[i]
        _USERLINE = retrieve_userChamp_data(_USERCHAMP, inFile)
        outList = compute_similarity_scores(inFile, _USERLINE)
        print("For the champion: ", _USERCHAMP)
        organize_output_list_SHORT(outList)
    print(outList)
        
    #housekeeping
    inFile.close()
   
if __name__ == '__main__':
    main()