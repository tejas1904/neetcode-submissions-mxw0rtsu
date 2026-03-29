class Solution:
    def trap(self, height: List[int]) -> int:
         
        max_height_to_left_of_pos = []
        maxH = 0

        for i in range(len(height)):
            h = height[i]
            if h>maxH:
                maxH = h
            max_height_to_left_of_pos.append(maxH)

        max_height_to_right_of_pos = [0] * len(height)
        maxH = 0
        for i in range(len(height)-1 ,-1 ,-1):
            h = height[i]
            if h>maxH:
                maxH = h
            max_height_to_right_of_pos[i] =maxH
        
        fillable = [0] * len(height)
        for i in range(len(height)):
            h = height[i]
            fillable[i] = (min(max_height_to_left_of_pos[i] ,max_height_to_right_of_pos[i]) - h)
        
        summ = 0
        for item in fillable:
            summ  = (summ+item) if item>0 else summ
        return summ

        

        
            
        