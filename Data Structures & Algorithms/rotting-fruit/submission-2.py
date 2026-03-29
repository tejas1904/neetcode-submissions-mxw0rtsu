class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)-1
        cols = len(grid[0])-1
        visited = set()

        def isValid(i,j):
            if (0<=i<=rows) and (0<=j<=cols) and grid[i][j]==1 and (i,j) not in visited:
                return True
            else:
                return False

        def multiSourceBFS():
            
            queue = deque()
            
            totalfresh = 0
            for i in range(rows+1):
                for j in range(cols+1):
                    if grid[i][j]==2:
                        queue.append((i,j))
                        visited.add((i,j))#rotten by adding to visited
                    if grid[i][j]==1:
                        totalfresh +=1
            
            levels = 0
            while queue:
                smethingWasAbleToRot = False
                for _ in range(len(queue)):
                    x,y = queue.popleft()
                    for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                        nx,ny = x+dx,y+dy
                        if isValid(nx,ny):
                            smethingWasAbleToRot = True
                            visited.add((nx,ny)) #rotting by adding to visited
                            totalfresh = totalfresh-1
                            queue.append((nx,ny))
                
                if smethingWasAbleToRot:        
                    levels = levels+1
            
        
            if totalfresh==0:
                return levels
            else:
                return -1
        
        return multiSourceBFS()

            


        