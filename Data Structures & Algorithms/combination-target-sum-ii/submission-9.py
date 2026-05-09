class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        nums = candidates
        ans = []
        arr = []

        def bktrak(start,summ):
            nonlocal ans
            nonlocal arr
            if summ==target:
                ans.append(arr.copy())
                return
            if summ>target or start==len(nums):
                return
            
            for i in range(start,len(nums)):
                if i>start and nums[i-1]==nums[i]:
                    continue
                arr.append(nums[i])
                bktrak(i+1, summ+nums[i])
                arr.pop(-1)
        
        bktrak(0,0)
        return ans
            
            
            

