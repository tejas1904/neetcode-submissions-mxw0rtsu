class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        ans = []
        arr = []
        def bktrak(i):
            nonlocal ans
            nonlocal arr
            if i==len(nums):
                ans.append(arr.copy())
            else:
                bktrak(i+1)
                
                arr.append(nums[i])
                bktrak(i+1)
                arr.pop()

        bktrak(i=0)
        return ans