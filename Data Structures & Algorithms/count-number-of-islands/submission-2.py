class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = {}
        rows = len(grid)
        cols = len(grid[0])

        tc = 0


        def exploreBFS(i,j):
            def isValid(i,j):
                if (not (0<=i and i<=rows-1)) or (not (0<=j and j<=cols-1)):
                    return False
                if grid[i][j] == "0":
                    return False
                if visited.get((i,j),False)==True:
                    return False
                return True
            
            queue = deque()
            queue.append((i,j))
            while queue:
                elem_x , elem_y = queue.popleft()
                visited[(elem_x , elem_y)] = True
                for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                    nx ,ny = elem_x+dx , elem_y+dy
                    if isValid(nx,ny):
                        queue.append((nx,ny))
                    


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (grid[i][j]=="1") and (visited.get((i,j),False)==False):
                    exploreBFS(i,j)
                    tc = tc + 1
        
        return tc



        