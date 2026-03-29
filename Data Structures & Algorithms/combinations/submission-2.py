class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        temp = []

        def dfs(start):
            if len(temp)==k: #if size is same match append 
                ans.append(temp.copy())
            if start>n or len(temp)>k:
                return

            else:
                for ind in range(start,n+1): #to prevent duplicated at each level only look forward
                    temp.append(ind)
                    dfs(ind+1)
                    temp.pop(-1)
        
        dfs(1)
        return ans
