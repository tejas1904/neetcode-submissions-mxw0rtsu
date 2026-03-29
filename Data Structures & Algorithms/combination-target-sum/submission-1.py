from typing import List

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        
        def helper(arr: List[int], currentSum: int, i: int):
            if currentSum == target:
                ans.append(arr[:]) 
                return
            for j in range(i, len(nums)):
                num = nums[j]
                if num <= (target - currentSum):
                    arr.append(num)
                    helper(arr, currentSum + num, j)  
                    arr.pop()  # Backtrack
        
        helper([], 0, 0) 
        return ans
