class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        tsum = 0
        def bktrak(i,res):
            nonlocal tsum
            if i==len(nums):
                tsum+=res 
            else:
                bktrak(i+1,res)
                bktrak(i+1,res^nums[i])
        bktrak(0,0)
        return tsum
        