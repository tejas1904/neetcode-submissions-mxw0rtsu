class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans,arr = [],[]
        def bktrak(start):
            nonlocal arr
            nonlocal ans
            if len(arr)==k:
                ans.append(arr.copy())
                return
            
            for i in range(start,n+1):
                arr.append(i)
                bktrak(i+1)
                arr.pop(-1)
            
        bktrak(1)
        return ans
        