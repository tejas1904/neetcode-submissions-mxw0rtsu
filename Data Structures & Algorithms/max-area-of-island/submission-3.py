class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)-1
        cols = len(grid[0])-1

        visited = set()
        self.area = 0 
        self.MaxArea = 0
        def exploreDFS(i,j):
            if not(0<=i and i<=rows) or not(0<=j and j<=cols):
                return
            if (i,j) in visited:
                return
            if grid[i][j]==0:
                return
            
            visited.add((i,j))
            self.area += 1

            for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                exploreDFS(i+dx,j+dy)

        for i in range(rows+1):
            for j in range(cols+1):
                if grid[i][j]==1 and (i,j) not in visited:
                    self.area = 0  
                    exploreDFS(i,j)
                    self.MaxArea = max(self.MaxArea,self.area)
        
        return self.MaxArea



            
