class Solution:
    def maxArea(self, heights: List[int]) -> int:
        hashSet = {}
        def MaxArea(l,r):
            if l>=r:
                return 0
            if (l,r) in hashSet:
                return hashSet[(l,r)]
            else:
                curretArea = min(heights[l],heights[r])*(r-l)
                bestArea =  max(curretArea, MaxArea(l+1,r) , MaxArea(l,r-1))
                hashSet[(l,r)]  = bestArea
                return bestArea


        
        return MaxArea(0,len(heights)-1)
        
        
        