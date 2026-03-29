class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows=len(matrix)
        cols=len(matrix[0]) 
        l=0
        r=rows-1

        row = None
        while l<=r:
            mid=(l+r)//2
            if matrix[mid][0]<=target<=matrix[mid][cols-1]:
                row = mid
                break
            
            if target<matrix[mid][0]:
                r=mid-1
            elif matrix[mid][cols-1]<target:
                l=mid+1
        
        if row == None:
            return False
        
        arr=matrix[row]
        l=0
        r=len(arr)-1
        while l<=r:
            mid = (l+r)//2
            if arr[mid]==target:
                return True
            elif target<arr[mid]:
                r=mid-1
            elif arr[mid]<target:
                l=mid+1
        
        return False
        
        


        