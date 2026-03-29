class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        count = 0
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        
        def dfs_count(i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 1 and not visited[i][j]:
                visited[i][j] = True
                area = 1 
                for a, b in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    area += dfs_count(a, b)
                return area
            return 0
        
        maxi = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and not visited[i][j]:
                    ret = dfs_count(i, j)
                    maxi = max(maxi, ret) 
        
        return maxi
