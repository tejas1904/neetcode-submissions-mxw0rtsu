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
                #we porcess the first duplicate element and skip the rest of them
                arr.append(candidates[x])
                backtrack(x+1)
                arr.pop()

                while x+1 < len(candidates) and candidates[x]==candidates[x+1]:
                    x+=1
                x+=1
        backtrack(0)
        return ans

# At the same recursion level, if you use a duplicate element,
# it will produce identical sub-problems that were already explored
# in the previous duplicate's recursion tree,
# so we only need to explore the first occurrence.

        