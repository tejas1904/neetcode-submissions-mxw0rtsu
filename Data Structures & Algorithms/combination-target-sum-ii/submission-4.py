class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        subarr = []
        
        def dfs(i,summ):
            if summ==target:
                ans.append(subarr.copy())
                return
            elif summ>target:
                return
            elif i==len(candidates):
                return
            else:
                
                x=i
                while x<len(candidates)-1 and candidates[x]==candidates[x+1]:
                    x+=1
                    
                dfs(x+1,summ+0)

                subarr.append(candidates[i])
                dfs(i+1,summ+candidates[i])
                subarr.pop()
        dfs(0,0)
        return ans

        
        