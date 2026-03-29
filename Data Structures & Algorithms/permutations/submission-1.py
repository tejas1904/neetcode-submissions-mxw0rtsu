class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        subarr = []
        arr = []

        seen_index = set()
        def dfs():
            if len(subarr)==len(nums):
                arr.append(subarr.copy())
            else:
                for i in range(len(nums)):
                    if i not in seen_index:
                        seen_index.add(i)
                        subarr.append(nums[i])
                        dfs()
                        subarr.pop()
                        seen_index.remove(i)
        
        dfs()
        return arr
                    