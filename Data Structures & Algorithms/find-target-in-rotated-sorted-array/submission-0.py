class Solution:
    def search(self, arr: List[int], target: int) -> int:
        l=0
        r=len(arr)-1
        while l<=r:
            mid = (l+r)//2
            if target == arr[mid]:
                return mid
            
            if arr[mid]<arr[r]:
                if arr[r]<target or target<arr[mid]:
                    r=mid-1
                else:
                    l=mid+1
            else:
                if arr[mid]<target or target<arr[l]:
                    l=mid+1
                else:
                    r=mid-1
    

        return -1
        