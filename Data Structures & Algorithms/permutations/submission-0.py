class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        arr = []
        seen_index = set()
        def backtrack():
            if len(arr)>=len(nums):
                ans.append(arr.copy())
                return

            for i in range(0,len(nums)):
                if i not in seen_index:
                    seen_index.add(i)
                    arr.append(nums[i])
                    backtrack()
                    arr.pop()
                    seen_index.remove(i)
        
        backtrack()
        return ans
                