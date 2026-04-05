class Solution:
    def jump(self, nums: List[int]) -> int:
        minJumpsFrom = [float('inf')]*len(nums)
        minJumpsFrom[-1] = 0

        for i in range(len(nums)-2, -1, -1):
            for jumplen in range(1,nums[i]+1,1):
                if i+jumplen < len(nums):
                    minJumpsFrom[i] = min(minJumpsFrom[i],1+minJumpsFrom[i+jumplen])
        
        return minJumpsFrom[0]
