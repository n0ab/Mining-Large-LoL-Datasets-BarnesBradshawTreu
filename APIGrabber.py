# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 13:34:18 2020

@author: Noah
"""


from riotwatcher import LolWatcher, ApiError
import sys

class APIGrabber():
    
    #global variables/commands
    api_key =  'RGAPI-1eccb832-1061-448c-8f28-86bb40735b63'
    watcher = LolWatcher(api_key)
    my_region = 'na1'
    sys.tracebacklimit = 0
    
    #Stat Grabbers
    dict = watcher.summoner.by_name(my_region, 'Wooglin')
    summonerID = dict.get('id')
    print(summonerID)
    
    #my_ranked_stats = watcher.league.by_summoner(my_region, me['id'])
    #print(my_ranked_stats)
    