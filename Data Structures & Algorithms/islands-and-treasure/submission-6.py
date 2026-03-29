class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        rows = len(grid)-1
        cols = len(grid[0])-1
        visited =set()
    

        def isValid(i,j):
            if 0<=i<=rows and 0<=j<=cols and grid[i][j]!=-1 and grid[i][j]!=0 and ((i,j)not in visited):
                return True
            else:
                return False

        def multiSourceBFS():
            queue = deque()

            for i in range(rows+1):
                for j in range(cols+1):
                    if grid[i][j] == 0:
                        queue.append((i,j))
                        visited.add((i,j))
            level = 1
            while queue:
                for _ in range(len(queue)):
                    x,y = queue.popleft()
                    for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                        nx,ny = x+dx , y+dy
                        if isValid(nx,ny):
                            grid[nx][ny] = min(level,grid[nx][ny])
                            queue.append((nx,ny))
                            visited.add((nx,ny))

                level = level+1
        
        multiSourceBFS()
        
        