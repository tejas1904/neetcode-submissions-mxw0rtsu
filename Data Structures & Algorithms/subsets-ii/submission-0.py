class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        arr = []

        def backtrack(i):

            if i>=len(nums):
                ans.append(arr.copy())
                return
            
            #dont include anything and skip to the next non repeat
            j = i
            while (j+1<len(nums) and nums[j]==nums[j+1]):
                j+=1
            j+=1 #after this j is at next non duplicate pos
            backtrack(j)

            arr.append(nums[i])
            backtrack(i+1)
            arr.pop()
        
        backtrack(0)
        return ans

