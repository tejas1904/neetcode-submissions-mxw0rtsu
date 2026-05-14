import functools
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows,cols = len(obstacleGrid)-1,len(obstacleGrid[0])-1
        count = 0
        @functools.lru_cache(None)
        def dfs(x,y):
            if not(0<=x<=rows) or not(0<=y<=cols):
                return 0
            if obstacleGrid[x][y]==1:
                return 0

            if x==rows and y==cols:
                return 1
            
            return dfs(x+1,y)+dfs(x,y+1)
        
        return dfs(0,0)
