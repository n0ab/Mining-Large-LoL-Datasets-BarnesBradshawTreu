# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 18:08:46 2020
Outputs the total "style" points per archetype.
"Style" is the reliance of one champion on either basic
attacks or abilities. The higher the style, the more
reliance on abilities rather than basic attacks.

@author: nbarnes
"""


from mrjob.job import MRJob

class HardestArchetype(MRJob):
    def mapper(self, key, line):
        (name, archetype, style) = line.split(',')       
        yield archetype, style
    
    def reducer(self, archetype, style): 
        #style = int(style)
        yield archetype, sum(style)
    
if __name__ == '__main__':
    HardestArchetype.run()