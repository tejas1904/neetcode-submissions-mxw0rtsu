class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        countDict={}
        for num in hand:
            if num in countDict:
                countDict[num]+=1
            else:
                countDict[num]=1
        
        keys = sorted(countDict.keys())

        for num in keys:
            while countDict[num]>0:
                countDict[num]-=1

                for nxt in range(num+1,num+groupSize):
                    if nxt in countDict.keys() and countDict[nxt]!=0:
                        countDict[nxt]-=1
                    else:
                        return False
        
        return True
            
