class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n==0:
            return 0
        if n==1:
            return nums[-1]
        if n==2:
            return max(nums[-2],nums[-1])
    
        cache = [0 for _ in range(n)]
        
        cache[-1] = nums[-1]
        cache[-2] = max(nums[-2]+0 , nums[-1])

        for i in range(n-3,-1,-1):
            cache[i] = max(
                nums[i] + cache[i+2],
                cache[i+1]
            )
        return cache[0]