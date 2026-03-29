class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def bktrak(arr,i):
            if i==len(nums):
                ans.append(arr.copy())
            else:
                bktrak(arr+[nums[i]],i+1)
                bktrak(arr,i+1)

        bktrak([],0)

        return ans
