class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        arr = []
        ans = []

        def backtrack(i):
            if i>len(candidates):
                return
            if sum(arr)==target:
                ans.append(arr.copy())
                return
            
            x=i
            while x<len(candidates):
                if x>i and candidates[x-1]==candidates[x]:
                    x+=1
                else:
                    arr.append(candidates[x])
                    backtrack(x+1)
                    arr.pop()
                    x+=1
        backtrack(0)
        return ans

        