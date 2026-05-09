class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans,arr = [],[]
        def bktrak(avail):
            nonlocal arr
            nonlocal ans
            if len(avail)==0:
                ans.append(arr.copy())
                return
            
            for num in avail.copy():
                arr.append(num)
                avail.remove(num)
                bktrak(avail.copy())
                avail.add(num)
                arr.pop(-1)
        bktrak(set(nums))
        return ans
        