class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zeroCount = 0
        for num in nums:
            if num!=0:
                prod = prod*num
            else:
                zeroCount +=1
        if zeroCount>=2:
            return [0 for i in range(len(nums))]
        if zeroCount==1:
            for i in range(len(nums)):
                if nums[i]==0:
                    nums[i] = prod
                else:
                    nums[i] = 0
            return nums
        else:
            for i in range(len(nums)):
                nums[i] = int(prod/nums[i])
            return nums

        