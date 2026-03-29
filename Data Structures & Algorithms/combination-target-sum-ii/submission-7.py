class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        ans = []

        def bktrak(i,arr):
            if sum(arr)==target:
                ans.append(arr.copy())
            if sum(arr)>target:
                return 
            else:
                for j in range(i,len(nums)):
                    if j>i and nums[j-1]==nums[j]:
                        continue
                    
                    bktrak(j+1,arr+[nums[j]])
                    
                    
        
        bktrak(0,[])
        return ans
        