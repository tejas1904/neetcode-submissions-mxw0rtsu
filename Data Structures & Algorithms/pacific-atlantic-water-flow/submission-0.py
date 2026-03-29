class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        rows = len(heights)-1
        cols = len(heights[0])-1

        pacificFlowUp = [[0]*(cols+1) for _ in range(rows+1)] 
        atlanticFlowUp = [[0]*(cols+1) for _ in range(rows+1)] 

        def isValid(matrix,x,y):
            if (0<=x<=rows) and (0<=y<=cols) and matrix[x][y]==0:
                return True
            return False

        def bfs(grid):
            queue = deque()
            for i in range(rows+1):
                for j in range(cols+1):
                    if grid[i][j] == 1:
                        queue.append((i,j))
            
            while queue:
                x,y = queue.popleft()
                for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                    
                    nx,ny = x+dx , y+dy
                    
                    if isValid(grid,nx,ny):
                        
                        if heights[nx][ny]>=heights[x][y]:
                            queue.append((nx,ny))
                            grid[nx][ny]= 1 

        #pacifc immediate neighbours fill with ones
        for i in range(rows+1):
            pacificFlowUp[i][0] = 1
        for j in range(cols+1):
            pacificFlowUp[0][j] = 1
        bfs(pacificFlowUp)

        #atlantic immediate neighbours fill with ones
        for i in range(rows+1):
            atlanticFlowUp[i][-1] = 1
        for j in range(cols+1):
            atlanticFlowUp[-1][j] = 1
        bfs(atlanticFlowUp)
        
        ans = []
        for i in range(rows+1):
            for j in range(cols+1):
                if pacificFlowUp[i][j]==atlanticFlowUp[i][j]==1:
                    ans.append([i,j])
        
        return ans

        
        
        
