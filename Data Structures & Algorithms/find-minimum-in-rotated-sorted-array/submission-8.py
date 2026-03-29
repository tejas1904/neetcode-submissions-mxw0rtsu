class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1

        while l<r:
            mid = (l+r)//2
            if nums[mid]<nums[r]:#array from mid to right is sorted
                r=mid
            elif nums[l]<=nums[mid]:#array from left to mid is sorted
                l=mid+1
        
        return nums[r]