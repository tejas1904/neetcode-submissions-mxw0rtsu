class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ans=[]
        arr=[]

        def bktrak(start):
            if start>len(nums):
                return
            else:
                ans.append(arr.copy())
                for i in range(start,len(nums)):
                    if i>start and nums[i-1]==nums[i]:
                        continue
                    else:
                        arr.append(nums[i])
                        bktrak(i+1)
                        arr.pop(-1)
        bktrak(0)
        return ans