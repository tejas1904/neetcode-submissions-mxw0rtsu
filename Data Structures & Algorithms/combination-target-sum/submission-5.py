class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans=[]
        def bktrak(i,arr,summ):
            nonlocal ans
            if summ==target:
                ans.append(arr.copy())
                return
            elif summ>target:
                return
            
                
            for start in range(i,len(nums)):
                arr.append(nums[start])
                bktrak(start,arr,summ+nums[start])
                arr.pop(-1)
        bktrak(i=0,arr=[],summ=0)
        return ans
        