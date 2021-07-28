# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 12:23:29 2020

@author: Noah
"""

from mrjob.job import MRJob

class SimilarChamps(MRJob):
    #STEPS
    #-----------------------------
    #Compute the Similarity
    #Ask for input of a single champion, return a list of similar champions
    
    #global variable declaration
    global user_champ
    global _CHAMPNAME
    global _CHAMPLIST
    
    def ask_for_input():
        print("This program will give you similar champions to a champion you like.")
        champ = input("Please enter which champion you most enjoy, omit spaces and punctuation please!")
        return champ
    
    #global variable assigment
    user_champ = ask_for_input()
    
    def mapper_parse_input(self, key, line):
        #breaks up input file into usable pieces, denoted as (name, attributes)
        (name,lane,role,damageType,hardCC,hardEngage,disengage,poke,waveclear,tank,game) = line.split(',')
        attributeList = line.split(',')
        #remove redundant first element of list --> name
        attributeList.pop()
        #returns name, [attributes]
        yield name, attributeList
        
    def find_user_champ_name(name, attributeList):
        if (name == user_champ):
            CHAMP_NAME = name
            return CHAMP_NAME
        
    def find_user_champ_attributes(name, attributeList):
        if (name == user_champ):
            CHAMP_ATTRIBUTE_LIST = attributeList
            return CHAMP_ATTRIBUTE_LIST
    
    #more global variable assignments
    _CHAMPNAME = find_user_champ_name()
    _CHAMPLIST = find_user_champ_attributes()
    
    def mapper_base_similarity_builder(self, name, attributeList):
        #check for lane similarity
        if (attributeList[0] == _CHAMPLIST[0]):
            #check for role similarity
            if(attributeList[1] == _CHAMPLIST[1]):
            #check for damage similarity
                if(attributeList[2] == _CHAMPLIST[2]):
                    yield name, attributeList
    
    
    def compute_similar_deltas(name, attributeList):
        scoreList = attributeList[3:9]
        globalScoreList = _CHAMPLIST[3:9]
        #for parsing scoreList and globalScoreList
        i = 0
        #delta score
        score = 0
        #in the array
        while (i != 8):
            for i in scoreList:
                #if champion possesses same attributes, add to champion "similarity score"
                if(scoreList[i] == globalScoreList[i]):
                    score += 1
        yield name, score
        
    def reducer_identity(self, name, score):
        yield name, score
            
if __name__ == '__main__':
    SimilarChamps.run()