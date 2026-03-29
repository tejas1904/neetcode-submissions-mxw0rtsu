class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = float('-inf')
        for n in range(0,len(nums)):
            i=0
            j=i+n
            sum=0
            for k in range(i,j+1):
                sum=sum+nums[k]
            
            maxsum= max(sum,maxsum)
            while (j<=len(nums)-2):
                sum = sum-nums[i]
                i+=1
                j+=1
                sum = sum+nums[j]
                maxsum= max(sum,maxsum)
        return int(maxsum)


        