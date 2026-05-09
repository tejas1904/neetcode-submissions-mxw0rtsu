class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        numCount = {}
        for num in nums:
            numCount[num] = numCount.get(num,0)+1

        ans,arr = [],[]
        def bktrak():
            nonlocal arr
            nonlocal ans
            nonlocal numCount
            if len(arr)==len(nums):
                ans.append(arr.copy())
                return

            for key in numCount.keys():
                if numCount[key]>0:
                    arr.append(key)
                    numCount[key]-=1
                    bktrak()
                    numCount[key]+=1
                    arr.pop(-1) 
        bktrak()
        return ans