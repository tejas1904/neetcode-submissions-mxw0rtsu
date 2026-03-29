class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        h=len(heights)-1
        def getArea(l,h):
            return (h-l) * min(heights[l],heights[h])

        maxArea = getArea(l,h)

        while l<h:
            if heights[l]<heights[h]:
                l =l+1
            else:
                h=h-1
            maxArea = max(maxArea,getArea(l,h))
        
        return maxArea
            

        