class Solution:
    def search(self, nums: List[int], target: int) -> int:

        
        def BinarySearch(L,R):
            while L<=R:
                mid = (L+R)//2
                if nums[mid]==target:
                    return mid
                
                if target>nums[mid]:
                    L=mid+1
                if target<nums[mid]:
                    R=mid-1
            return -1

        return BinarySearch(0,len(nums)-1)