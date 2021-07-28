# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 11:40:56 2020
Returns 148  matches' winning and losing teams and their champions picked

@author: Noah
"""

#imports
from riotwatcher import LolWatcher
import sys

#global variables + misc.
global api_key
global watcher
global my_region
global inFile
api_key =  'RGAPI-409e7dbd-7dd4-4aab-be8b-d3ca4361d595'
watcher = LolWatcher(api_key)
my_region = 'na1'
inFile = open('C:/Users/Noah/matchIDs.txt', 'r')
sys.tracebacklimit = 0



def get_summoner_match_list(string):
    out = []
    dict = watcher.summoner.by_name(my_region, string)
    encryptedID = dict.get('accountId')
    dict = watcher.match.matchlist_by_account(my_region, encryptedID)
    matchesList = dict.get('matches')
    for dict in matchesList:
        matchID = dict.get('gameId')
        out.append(matchID)
    return out



def get_match_info(inList):
    finalOut = []
    for ID in inList:
        matchID = ID
        dict = watcher.match.by_id(my_region, matchID)
        teamsDict = dict.get('teams')
        winner = ''
        if teamsDict[0].get('win') == 'Win':
            winner = 100
        else:
            winner = 200
        participantsDict = dict.get('participants')
        tempWinners = []
        tempLosers = []
        for i in range(len(participantsDict)):
            #print("TEAM ID: ", participantsDict[i].get('teamId'))
            teamID = participantsDict[i].get('teamId')
            if teamID == winner:
                tempWinners.append(participantsDict[i].get('championId'))
            if teamID != winner:
                tempLosers.append(participantsDict[i].get('championId'))
        finalOut.append("winner")
        finalOut.append(tempWinners)
        finalOut.append("loser")
        finalOut.append(tempLosers)
    return finalOut


def get_match_info_WINNERS(inList):
    finalOut = []
    for ID in inList:
        matchID = ID
        dict = watcher.match.by_id(my_region, matchID)
        teamsDict = dict.get('teams')
        winner = ''
        if teamsDict[0].get('win') == 'Win':
            winner = 100
        else:
            winner = 200
        participantsDict = dict.get('participants')
        tempWinners = []
        tempLosers = []
        for i in range(len(participantsDict)):
            #print("TEAM ID: ", participantsDict[i].get('teamId'))
            teamID = participantsDict[i].get('teamId')
            if teamID == winner:
                tempWinners.append(participantsDict[i].get('championId'))
            if teamID != winner:
                tempLosers.append(participantsDict[i].get('championId'))
        finalOut.append("winner")
        finalOut.append(tempWinners)
    return finalOut


def get_match_info_LOSERS(inList):
    finalOut = []
    for ID in inList:
        matchID = ID
        dict = watcher.match.by_id(my_region, matchID)
        teamsDict = dict.get('teams')
        winner = ''
        if teamsDict[0].get('win') == 'Win':
            winner = 100
        else:
            winner = 200
        participantsDict = dict.get('participants')
        tempWinners = []
        tempLosers = []
        for i in range(len(participantsDict)):
            #print("TEAM ID: ", participantsDict[i].get('teamId'))
            teamID = participantsDict[i].get('teamId')
            if teamID == winner:
                tempWinners.append(participantsDict[i].get('championId'))
            if teamID != winner:
                tempLosers.append(participantsDict[i].get('championId'))
        finalOut.append("loser")
        finalOut.append(tempLosers)
    return finalOut

def organize_output(inList):
    for p in inList:
        if isinstance(p, list):
            print(*p)
            continue
        else:
            print(p, end = " ")
        
            
    
def main():
    inString = "GGradate"
    inList = get_summoner_match_list(inString)
    finalList = get_match_info_LOSERS(inList)
    print(organize_output(finalList))
    


if __name__ == "__main__":
    main()