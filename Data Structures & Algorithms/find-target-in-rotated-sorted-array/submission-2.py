class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0,len(nums)-1
        while l<=r:
            mid=(l+r)//2
            if target==nums[mid]:
                return mid
            
            if nums[mid]<nums[r]: #part to right of mid is sorted
                # when do i need to search the non scrictly increasing part
                if target>nums[r] or target<nums[mid]:
                    r=mid-1
                else:
                    l=mid+1
            
            elif nums[l]<=nums[mid]: #array to left of mid is sorted
                # when to search the right unsorted part:
                if target<nums[l] or nums[mid]<target:
                    l=mid+1
                else:
                    r=mid-1
        return -1

        