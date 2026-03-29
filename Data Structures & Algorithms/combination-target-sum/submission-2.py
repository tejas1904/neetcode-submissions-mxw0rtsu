class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        temp=[]
        def dfs(currsum,i):
            if currsum>target:
                return
            elif currsum==target:
                res.append(temp.copy())
            else:
                for k in range(i,len(nums)):
                    temp.append(nums[k])
                    dfs(currsum + nums[k], k)
                    temp.pop(-1)

        dfs(currsum=0,i=0)
        return res