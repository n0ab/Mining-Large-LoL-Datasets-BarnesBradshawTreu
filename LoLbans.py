# To run locally:
# !python LoLBans.py bans > bansoutput.txt

# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 16:53:17 2020
LoLBans outputs which champions were banned the most from the input document

@author: nbarnes
"""


from mrjob.job import MRJob

class LoLBans(MRJob):
    def mapper(self, key, line):
        inFile = open('C:/Users/Noah/champdatashort.txt', 'r')
        for line in inFile:
            try:
                (Address, Team, ban_1, ban_2, ban_3, ban_4, ban_5) = line.split(',')
                champList = [ban_1, ban_2, ban_3, ban_4, ban_5] 
            except ValueError:
                continue
            yield champList, 1


    def reducer(self, champList, occurences):
        total = 0
        for champ in champList:
            yield champ, sum(occurences)

if __name__ == '__main__':
    LoLBans.run()
