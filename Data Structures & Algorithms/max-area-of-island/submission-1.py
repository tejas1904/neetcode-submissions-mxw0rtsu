class Solution:
    
    def maxAreaOfIsland(self, grid: List[List[str]]) -> int:
        count = 0
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        
        def bfs(i, j):
            queue = [[i, j]] 
            visited[i][j] = True
            i = 0
            while i<len(queue):
                a, b = queue[i]
                for x, y in ([a + 1, b], [a - 1, b], [a, b + 1], [a, b - 1]):
                    if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 1 and not visited[x][y]:
                        visited[x][y] = True
                        queue.append([x, y])
                i+=1
            return len(queue)
        maxi = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and not visited[i][j]:
                    ret = bfs(i, j)
                    if ret>maxi:
                        maxi=ret
        
        return maxi
