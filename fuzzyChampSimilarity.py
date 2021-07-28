import difflib


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
    with inFile as currFile:
        line = currFile.readline()
        for line in currFile:
            temp = line.split(',')
            champName = temp[0]
            temp.pop()
            score = difflib.SequenceMatcher(None, _USERLINE, line)
            scoreOut = score.ratio() * 100
            out.append(champName)
            out.append(int(scoreOut))
    return out
    
def organize_output_list(out):
    out = []
    champNames = []
    champScores = []
    for obj in out:
        if(isinstance(obj, str)):
            champNames.append(obj)
        else:
            champScores.append(int(obj))
    for i in range(len(champScores)):
        if champScores[i] == 100:
            champScores[i] = 0
    largestScoreIndex = champScores.index(max(champScores))
    
    return print("The champion you would most likely also enjoy based on your input is " + champNames[largestScoreIndex])
                
def main():
    _USERCHAMP = "Warwick"
    _USERLINE = retrieve_userChamp_data(_USERCHAMP, inFile)
    outList = compute_similarity_scores(inFile, _USERLINE)
    print(organize_output_list(outList))
    #print(outList)
    inFile.close()
   
if __name__ == '__main__':
    main()