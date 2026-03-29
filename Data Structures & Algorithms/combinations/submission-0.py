class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        temp = []

        def dfs(i):
            if len(temp)==k:
                ans.append(temp.copy())
            if i>n or len(temp)>k:
                return

            else:
                for ind in range(i,n+1):
                    temp.append(ind)
                    dfs(ind+1)
                    temp.pop(-1)
        
        dfs(1)
        return ans
