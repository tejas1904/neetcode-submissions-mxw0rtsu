class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        r=len(heights)-1

        maxArea = -float('inf')

        while l<r:
            currArea = min(heights[l],heights[r])*(r-l)
            maxArea = max(maxArea,currArea)

            if heights[l]<heights[r]:
                l+=1
            else:
                r=r-1
        return maxArea