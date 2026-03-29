class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []

        def bktrak(i,arr):
            if sum(arr)==target:
                ans.append(arr.copy())
            if sum(arr)>target:
                return 
            else:
                for j in range(i,len(nums)):
                    bktrak(j,arr+[nums[j]])
        
        bktrak(0,[])
        return ans
        