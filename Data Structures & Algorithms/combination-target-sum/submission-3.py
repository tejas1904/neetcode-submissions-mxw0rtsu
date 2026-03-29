class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans  = []
        subarr = []

        def dfs(i,summ):
            if summ>target:
                return 
            elif summ==target:
                ans.append(subarr.copy())
            else:
                for x in range(i,len(nums)):
                    subarr.append(nums[x])
                    summ+=nums[x]

                    dfs(x,summ)

                    subarr.pop()
                    summ-=nums[x]
        dfs(0,0)
        return ans