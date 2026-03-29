class Solution:
    def jump(self, nums: List[int]) -> int:
        goal_pos = len(nums)-1
        min_jumps = [float('inf')]*len(nums)
        
        min_jumps[len(nums)-1] = 0
        
        for i in range(len(nums)-2,-1,-1):
            if (i+nums[i]) >= goal_pos:
                goal_pos = i
                
                l = i+1
                r = min(i+nums[i] , len(nums)-1)
                for j in range(l,r+1):
                    min_jumps[i] = min(min_jumps[i] ,min_jumps[j] )
                min_jumps[i]+=1

        return min_jumps[0]
