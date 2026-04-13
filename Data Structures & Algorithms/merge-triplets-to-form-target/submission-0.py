class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        #if we find any triplet having ith pos greater than target then dont consider it
        possibleTriplets = []
        for v1,v2,v3 in triplets:
            if v1>target[0] or v2>target[1] or v3>target[2]:
                pass
            else:
                possibleTriplets.append([v1,v2,v3])
        
        #if we fidnteh target[pos]caross any of the triplets
        possbility = [False,False,False]
        for v1,v2,v3 in possibleTriplets:
            if v1==target[0]:
                possbility[0]=True
            if v2==target[1]:
                possbility[1]=True
            if v3==target[2]:
                possbility[2]=True
        
        if possbility==[True,True,True]:
            return True
        else:
            return False

        

        
        