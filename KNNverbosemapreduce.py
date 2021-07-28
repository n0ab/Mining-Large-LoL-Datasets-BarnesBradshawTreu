# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 11:56:35 2020

@author: Noah
"""


from mrjob.job import MRJob
from mrjob.step import MRStep

class KNN(MRJob):
    
    def steps(self):
        return [
            MRStep(mapper=self.mapper_parse_input,
                    reducer=self.reducer_compute_similarity),
            ]
    
    def mapper_parse_input(self, key, line):
        tokens = line.split(',')
        champName = tokens[0]
        champAttributes = tokens[1:]
        yield champName, champAttributes
    
    
    def reducer_compute_similarity(self, champ, attributes):
        out = []
        
        #create a line list of the input champion
        
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
                
            #make sure lane is the most important score at +3
            if(attributeTemp[0] == _USERLINElist[0]):
                outScore += 3
                attributeTemp.pop(0)
                _USERLINElist.pop(0)
            
            
            
            #check for identical elements at the same indeces, if they are
            #identical, add a 1 to the final score
            for i in range(len(attributeTemp)):
                if _USERLINElist[i] == attributeTemp[i]:
                    outScore += 1.0
            out.append(champName)
            out.append(float(outScore))
        