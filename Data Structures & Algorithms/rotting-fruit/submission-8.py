class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        visited = [[False]*cols for _ in range(rows)]
        queue = []

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i,j))
  
        def isvalid(nx,ny):
            if 0<=nx and nx<=rows-1 and 0<=ny and ny<=cols-1:
                return True
            else:
                return False
        levels = 0

        while queue:
            levels+=1
            for _ in range(len(queue)):
                x,y = queue.pop(0)
                for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                    nx,ny = x+dx,y+dy
                    if isvalid(nx,ny) and grid[nx][ny]==1:
                        grid[nx][ny]=2
                        queue.append((nx,ny))
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return -1
        
        return levels-1 if levels>0 else  0
    








        