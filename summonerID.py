from riotwatcher import LolWatcher
import sys

#global variables
global api_key
global watcher
global my_region
global inFile
global sched
api_key =  'RGAPI-1eccb832-1061-448c-8f28-86bb40735b63'
watcher = LolWatcher(api_key)
my_region = 'na1'
inFile = open('C:/Users/Noah/LoLplayers18.txt', 'r')
sys.tracebacklimit = 0

    
def get_IDs_from_file(inFile):
    summoners = []
    encryptedIDs = []
    finalOutList = []
    with inFile as currFile:
        summoners = [line.rstrip() for line in currFile]
        for summoner in summoners:
            dict = watcher.summoner.by_name(my_region, summoner)
            summonerID = dict.get('id')
            encryptedIDs.append(summonerID)
            i = 141
    for ID in encryptedIDs:
        masteredChampions = []
        tempList = watcher.champion_mastery.by_summoner(my_region, ID)
        firstChamp = {}
        secondChamp = {}
        thirdChamp = {}
        firstChamp = tempList[0]
        secondChamp = tempList[1]
        thirdChamp = tempList[2]
        
        masteredChampions.append(i)
        champ = firstChamp.get('championId')
        champLevel = firstChamp.get('championLevel')
        champPoints = firstChamp.get('championPoints')
        masteredChampions.append(champ)
        masteredChampions.append(champLevel)
        masteredChampions.append(champPoints)
        
        masteredChampions.append(i)
        champ = secondChamp.get('championId')
        champLevel = secondChamp.get('championLevel')
        champPoints = secondChamp.get('championPoints')
        masteredChampions.append(champ)
        masteredChampions.append(champLevel)
        masteredChampions.append(champPoints)
        
        masteredChampions.append(i)
        champ = thirdChamp.get('championId')
        champLevel = thirdChamp.get('championLevel')
        champPoints = thirdChamp.get('championPoints')
        masteredChampions.append(champ)
        masteredChampions.append(champLevel)
        masteredChampions.append(champPoints)
        
        finalOutList.append(masteredChampions)
        i += 1
    return finalOutList


def list_output_formatting(inList):
    inFile = open('C:/Users/Noah/LoLplayers18.txt', 'r')
    inList = get_IDs_from_file(inFile)
    for currList in inList:
        tempListA = currList[0:4]
        tempListB = currList[4:8]
        tempListC = currList[8:13]
        print(*tempListA)
        print(*tempListB)
        print(*tempListC)
    return

def main():
    print(list_output_formatting(get_IDs_from_file(inFile)))
    
    
          
if __name__ == "__main__":
    main()