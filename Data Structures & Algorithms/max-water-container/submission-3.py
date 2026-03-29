class Solution:
    def maxArea(self, heights: List[int]) -> int:
        hashset={}
        def MaxArea(l,r):
            if l>=r:
                return 0
            if (l,r) in hashset:
                curretArea= hashset[(l,r)]
            else:
                curretArea = min(heights[l],heights[r])*(r-l)
                hashset[(l,r)] = curretArea
            return max(curretArea, MaxArea(l+1,r) , MaxArea(l,r-1))
        
        return MaxArea(0,len(heights)-1)
        
        
        