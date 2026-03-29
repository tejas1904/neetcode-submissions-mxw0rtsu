class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        rows = len(grid)-1
        cols = len(grid[0])-1
    

        def isValid(i,j,visited):
            if 0<=i<=rows and 0<=j<=cols and grid[i][j]!=-1 and grid[i][j]!=0 and ((i,j)not in visited):
                return True
            else:
                return False

        def bfs(i,j):
            
            visited = set()
            queue = deque([(i,j)])
            level = 1
            while queue:
                for _ in range(len(queue)):
                    node_x,node_y = queue.popleft()
                    for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                        x,y = node_x+dx, node_y+dy
                        if isValid(x,y,visited):
                            grid[x][y] = min(level,grid[x][y])
                            visited.add((x,y))
                            queue.append((x,y))
                    
                level = level+1


        for i in range(rows+1):
            for j in range(cols+1):
                if grid[i][j]==0:
                    bfs(i,j)