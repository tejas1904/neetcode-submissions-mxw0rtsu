class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = {}
        rows = len(grid)
        cols = len(grid[0])

        tc = 0


        def explore(i,j):
            if (not (0<=i and i<=rows-1)) or (not (0<=j and j<=cols-1)):
                return
            if grid[i][j] == "0":
                return
            if visited.get((i,j),False)==True:
                return
            else:
                visited[(i,j)] = True
                explore(i+1,j)
                explore(i-1,j)
                explore(i,j+1)
                explore(i,j-1)


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (grid[i][j]=="1") and (visited.get((i,j),False)==False):
                    explore(i,j)
                    tc = tc + 1
        
        return tc



        