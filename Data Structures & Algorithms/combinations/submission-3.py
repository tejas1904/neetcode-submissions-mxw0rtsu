class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        arr = []

        def backtrack(i):
            if len(arr)==k:
                ans.append(arr.copy())
                return
            
            for x in range(i,n):
                num = x+1
                arr.append(num)
                backtrack(x+1)
                arr.pop()
        
        backtrack(0)
        return ans

        