class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = {}
        def jg(pos):
            if pos in dp:
                return dp[pos]
            if pos==len(nums)-1:
                return True
            if nums[pos]==0:
                return False
            possible = False
            for jumps in range(1,nums[pos]+1):
                possible = possible or jg(pos+jumps)
            
            dp[pos] = possible
            return dp[pos]
        
        return jg(0)

            
