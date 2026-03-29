class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        subarr =[]

        def dfs(start):
            if sum(subarr)==target:
                ans.append(subarr.copy())
                return
            if start==len(candidates):
                return 
            else:
                for x in range(start,len(candidates)):
                    #At the same recursion depth, we only allow the first occurrence of a value.
                    if x>start and candidates[x-1]==candidates[x]:
                        continue
                    subarr.append(candidates[x])
                    dfs(x+1)
                    subarr.pop()
                    
        dfs(0)
        return ans 

            
