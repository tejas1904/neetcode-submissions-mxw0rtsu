class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        arr = []
        
        seen = set()

        def bktrak():
            if len(arr)==len(nums):
                ans.append(arr.copy())
            else:
                for i in range(len(nums)):
                    if i not in seen:
                        seen.add(i)
                        arr.append(nums[i])
                        
                        bktrak()
                        
                        arr.pop(-1)
                        seen.remove(i)
        
        bktrak()
        return ans
        