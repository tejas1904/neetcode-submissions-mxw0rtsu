class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1

        minNumber = float('inf')
        while l<=r:
            mid = (l+r)//2
            if nums[mid]<=nums[r]:#array from mid to right is sorted
                # the [mid] is the minimum element in the sequence [mid.....Right]
                # this could be the global minimum , so we store it and look left
                # we use a <= because in case of array of size 2 mid could be M==R so the last is still a sequence
                minNumber = min(minNumber,nums[mid])
                r=mid -1
            elif nums[l]<=nums[mid]:#array from left to mid is sorted
            # we use <= because if the L and mid element are the same then is should still work
            # this happens for a len(arr)=2 
                l=mid+1
        
        return minNumber