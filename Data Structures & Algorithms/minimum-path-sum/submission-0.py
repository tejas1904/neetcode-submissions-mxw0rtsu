import functools
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        r,c = len(grid)-1,len(grid[0])-1
        @functools.lru_cache(None)
        def dfs(x,y):
            if x==r and y==c:
                return grid[x][y]
            if x>r or y>c:
                return float('inf')
            else:
                return grid[x][y] +  min(
                    dfs(x+1,y),
                    dfs(x,y+1)
                )
        return dfs(0,0)
        