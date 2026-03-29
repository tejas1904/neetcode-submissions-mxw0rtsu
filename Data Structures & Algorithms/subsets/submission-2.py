class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        subarr = []
        
        def dfs(i):
            if i==len(nums):
                ans.append(subarr.copy())
                return
            
            dfs(i+1)

            subarr.append(nums[i])
            dfs(i+1)
            subarr.pop()
        
        dfs(0)
        return ans
        