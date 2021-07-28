# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 11:11:11 2020
Second build of champion similarity, uses Euclidean distance rather than SequenceMatcher
@author: Noah
"""


global inFile
inFile = open('C:/Users/Noah/champdata.txt', 'r')
    
#gets data for the user champion from the champion list
def retrieve_userChamp_data(_USERCHAMP, inFile):
    with inFile as currFile:
        line = currFile.readline()
        for line in currFile:
            if _USERCHAMP in line:
                return line
  
    
def compute_similarity_scores(inFile, _USERLINE):
    inFile = open('C:/Users/Noah/champdata.txt', 'r')
    out = []
    #create list of user champ attributes without the name
    _USERLINElist = _USERLINE.split(',')
    #_USERLINElist.pop(0)
    
    with inFile as currFile:
        line = currFile.readline()
        for line in currFile:
            _USERLINElist = _USERLINE.split(',')
            #_USERLINElist.pop(0)
            
            #create comma separated list of attributes including name
            attributeTemp = line.split(',')
            
            if(attributeTemp != _USERLINElist):
                #remove champion name and store in a temp variable
                champName = attributeTemp[0]
                attributeTemp.pop(0)
                _USERLINElist.pop(0)
                outScore = float(0)
                
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
                
                #lane: for sub vs obj
                if(attributeTemp[0] == _USERLINElist[0]):
                    outScore += 0
                    attributeTemp.pop(0)
                    _USERLINElist.pop(0)
                        
                #check for identical elements at the same indeces, if they are
                #identical, add a 1 to the final score
                for i in range(len(attributeTemp)):
                    if _USERLINElist[i] == attributeTemp[i]:
                        outScore += 1
                out.append(champName)
                out.append(float(outScore))
    return out
    
def organize_output_list(out):
    #
    champNames = []
    champScores = []
    for obj in out:
        if(isinstance(obj, str)):
            champNames.append(obj)
        else:
            champScores.append(float(obj))
            
    #change the score of the input champion to 0, as obviously the most similar
    #champion to the input is the same champion
    for i in range(len(champScores)):
        if champScores[i] == 12.5:
            champScores[i] = 0
    largestScoreIndex = champScores.index(max(champScores))
    return print("The champion you would most likely also enjoy based on your input is " + champNames[largestScoreIndex])


def organize_output_list_SHORT(out):
    #2 lists for organized output
    #print("OUT: ", out)
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
    inFile = open('C:/Users/Noah/champdata.txt', 'r')
    nameList = []
    with inFile as currFile:
        line = currFile.readline()
        for line in currFile:
            temp = line.split(',')
            name = temp[0]
            nameList.append(name)
    return nameList
                
def main():
    inFile = open('C:/Users/Noah/champdata.txt', 'r')
    
    #single input
    print("SINGLE INPUT:")
    _USERCHAMP = "Yasuo"
    #_USERLANE = "Support"
    _USERLINE = retrieve_userChamp_data(_USERCHAMP, inFile)
    #print(_USERLINE)
    outList = compute_similarity_scores(inFile, _USERLINE)
    print(organize_output_list_FIVE(outList))
    print(outList)
    
    """
    
    #every champion
    print("EVERY CHAMPION: ")
    champList = generate_nameList()
    for i in range(len(champList)):
        inFile = open('C:/Users/Noah/champdata.txt', 'r')
        _USERCHAMP = champList[i]
        _USERLINE = retrieve_userChamp_data(_USERCHAMP, inFile)
        outList = compute_similarity_scores(inFile, _USERLINE)
        #print(outList)
        print("For the champion: ", _USERCHAMP)
        print(organize_output_list_FIVE(outList))
   # print(outList)
     """
    inFile.close()
   
if __name__ == '__main__':
    main()