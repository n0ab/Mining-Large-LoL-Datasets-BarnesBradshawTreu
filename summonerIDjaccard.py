# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 12:24:01 2020

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


def compute_jaccard_distance(inFile, USERLINE, lane):
    inFile = open('C:/Users/Noah/champdataverbose.txt', 'r')
    out = []
    _USERLINElist = USERLINE.split(',')
    substring = lane
    with inFile as currFile:
        line = currFile.readline()
        for line in currFile:
            _USERLINElist = USERLINE.split(',')
            _USERLINElist.pop(0)
            if substring in line:
                OTHERCHAMPlist = line.split(',')
                champName = OTHERCHAMPlist[0]
                OTHERCHAMPlist.pop(0)
            
                #begin jaccard similarity
                set1 = set(_USERLINElist)
                set2 = set(OTHERCHAMPlist)
            
                outCalc = len(set1.intersection(set2)) / len(set1.union(set2))
                #end jaccard similarity
            
                out.append(champName)
                out.append(outCalc)
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
        if champScores[i] == 1.0:
            champScores[i] = 0
    largestScoreIndex = champScores.index(max(champScores))
    return print("The champion you would most likely also enjoy based on your input is " + champNames[largestScoreIndex])

def main():
    inFile = open('C:/Users/Noah/champdataverbose.txt', 'r')
    _USERCHAMP = "Nidalee"
    _USERLANE = "Jungle"
    _USERLINE = retrieve_userChamp_data(_USERCHAMP, inFile)
    outList = compute_jaccard_distance(inFile, _USERLINE, _USERLANE)
    print(organize_output_list(outList))
    print(outList)
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    count5 = 0
    count6 = 0
    count7 = 0
    count8 = 0
    count9 = 0
    for i in outList:
        if(type(i) is float and i == 1.0):
            count1 += 1
        if(type(i) is float and i == 0.3333333333333333):
            count2 += 1
        if(type(i) is float and i == 0.2222222222222222):
            count3 += 1
        if(type(i) is float and i == 0.2):
            count4 += 1
        if(type(i) is float and i == 0.7142857142857143):
            count5 += 1
        if(type(i) is float and i == 0.5):
            count6 += 1
        if(type(i) is float and i == 0.375):
            count7 += 1
        if(type(i) is float and i == 0.1):
            count8 += 1
        if(type(i) is float and i == 0.5714285714285714):
            count9 += 1
    print("Number of 1.0: ", count1)
    print("Number of 0.333...: ", count2)
    print("Number of 0.222...: ", count3)
    print("Number of 0.2: ", count4)
    print("Number of 0.7142857142857143: ", count5)
    print("Number of 0.5: ", count6)
    print("Number of 0.375: ", count7)
    print("Number of 0.1: ", count8)
    print("Number of 0.5714285714285714: ", count9)
    countSum = count1 + count2 + count3 + count4 + count5 + count6 + count7 + count8 + count9
    print("Total Champions Tested: ", countSum)

if __name__ == '__main__':
    main()