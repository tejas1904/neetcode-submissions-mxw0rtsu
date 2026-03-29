class Solution:
    def jump(self, nums: List[int]) -> int:
        n=len(nums)-1
        jumps = 0

        l=r=0

        while r<n:
            furthest = 0
            for i in range(l,r+1):
                furthest = max(furthest , i+nums[i])
            l=r+1
            r = furthest
            jumps+=1
        return jumps
            
