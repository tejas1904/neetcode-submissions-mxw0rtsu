class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowLow = 0
        rowHigh = len(matrix) - 1
        mid = None

        while rowLow<=rowHigh:
            mid =  (rowLow+rowHigh)//2

            if matrix[mid][0]<=target and target<=matrix[mid][-1]:
                break
            
            if target>matrix[mid][-1]:
                rowLow = mid+1
            elif target<matrix[mid][0]:
                rowHigh = mid -1
        row = mid
        low = 0
        high = len(matrix[0])-1
        mid = None

        while low<=high:
            mid = (low+high)//2
            if target == matrix[row][mid]:
                return True
            if target < matrix[row][mid]:
                high = mid - 1
            elif matrix[row][mid] < target:
                low = mid + 1

        return False