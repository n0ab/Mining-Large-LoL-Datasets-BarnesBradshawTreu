# To run locally:
# !python MovieSimilarities.py --items=ml-100k/u.item ml-100k/u.data > sims.txt

# To run on a single EMR node:
# !python MovieSimilarities.py -r emr --items=ml-100k/u.item ml-100k/u.data

# To run on 4 EMR nodes:
#!python MovieSimilarities.py -r emr --num-core-instances=3 --items=ml-100k/u.item ml-100k/u.data

# Troubleshooting EMR jobs (subsitute your job ID):
# !python -m mrjob.tools.emr.fetch_logs --find-failure j-1NXMMBNEQHAFT

#USE champdataverbosewhitespace.txt

from mrjob.job import MRJob
from mrjob.step import MRStep


class KNNmr(MRJob):

    def steps(self):
        return [
            MRStep(mapper=self.mapper_1,
                    reducer=self.reducer_1)]

    def mapper_1(self, key, line):
        (Name, Lane, Role, Damage, HardCC, HardEngage, Disengage, Poke, Waveclear, Tank, Mobility, 
                     Scaling, Snowball, Burst, Game, difficulty, manaless) = line.split(',')
        champName = Name
       
        yield champName, (Lane, Role, Damage, HardCC, HardEngage, Disengage, Poke, Waveclear, Tank, Mobility, 
                     Scaling, Snowball, Burst, Game, difficulty, manaless)



    def reducer_1(self, champName, attributes):
        finalOut = []
        out = []
        tempList = []
        tempList.append(champName)
        for attr in attributes:
            tempList.append(attr)
        out.append(tempList)
        outScore = float(0)
        for item in out:
            tempLine = item
            tempLineChampName = tempLine[0]
            tempLine.pop(0)
            itemChampTempName = item[0]
            item.pop(0)
            
            #if the current line list is not the userline
            if(tempLine != item):
                
                #manaless is important at 1.5
                if(item[15] == tempLine[15]):
                    outScore += 1.5
                    item.pop(15)
                    tempLine.pop(15)
                    
                #difficulty important at 2.0
                if(item[14] == tempLine[14]):
                    outScore += 2.0
                    item.pop(14)
                    tempLine.pop(14)
                
                #make sure game is an important score at +1.75
                if(item[13] == tempLine[13]):
                    outScore += 1.75
                    item.pop(13)
                    tempLine.pop(13)
                
                #create a 0.5 value for Poke and Waveclear if they are both true and flipped
                if((item[6] and tempLine[7] == '1') or (item[6] and tempLine[7] == '1')):
                    outScore += 0.5
                    item.pop(6)
                    item.pop(7)
                    tempLine.pop(6)
                    tempLine.pop(7)
                    
                #create a 0.5 value for HardCC and HardEngage if they are both true and flipped
                if((item[3] and tempLine[4] == '1') or (item[4] and tempLine[3] == '1')):
                    outScore += 0.5
                    item.pop(3)
                    item.pop(4)
                    tempLine.pop(3)
                    tempLine.pop(4)
                
                #make sure archetype is another important score at +1.5
                if(item[1] == tempLine[1]):
                    outScore += 1.5
                    item.pop(1)
                    tempLine.pop(1)
                    
                #make sure lane is the most important score at +3
                if(item[0] == tempLine[0]):
                    outScore += 3
                    item.pop(0)
                    tempLine.pop(0)
                
                
                finalOut.append("For Champion: ", itemChampTempName, ", NN are: ")
                #check for identical elements at the same indeces, if they are
                #identical, add a 1 to the final score
                for i in range(len(item)):
                    if item[i] == tempLine[i]:
                        outScore += 1.0
                
                finalOut.append(tempLineChampName)
                finalOut.append(float(outScore))
                
        yield finalOut



    """

    def reducer_1(self, champName, attributes):
        yield champName, attributes


    def mapper_1(self, key, line):
        # Outputs champID => (all stats)
        #(Name, Lane, Role, Damage, HardCC, HardEngage, Disengage, Poke, Waveclear, Tank, Mobility, 
         #Scaling, Snowball, Burst, Game, difficulty, manaless) = line.split('\t')
        #attributeList = [Lane, Role, Damage, HardCC, HardEngage, Disengage, Poke, Waveclear, Tank, Mobility, 
         #Scaling, Snowball, Burst, Game, difficulty, manaless]
        with open("C:/Users/Noah/champdataverbose.txt", encoding='ascii', errors='ignore') as inFile:
            for line in inFile:
                try:
                    (Name, Lane, Role, Damage, HardCC, HardEngage, Disengage, Poke, Waveclear, Tank, Mobility, 
                     Scaling, Snowball, Burst, Game, difficulty, manaless) = line.split(',')
                    attributes = [Lane, Role, Damage, HardCC, HardEngage, Disengage, Poke, Waveclear, Tank, Mobility, 
                     Scaling, Snowball, Burst, Game, difficulty, manaless] 
                    champName = Name
                except ValueError:
                    continue
                yield champName, attributes
    """

if __name__ == '__main__':
    KNNmr.run()
