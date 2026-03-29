class Solution:
    
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        def bfs(i,j):
            arr = [[i,j]]
            while arr:
                node = arr.pop(0)
                a,b = node[0],node[1]
                visited[a][b] = True
                for a,b in ([a+1,b],[a-1,b],[a,b+1],[a,b-1]):
                    if 0<=a<len(grid) and 0<=b<len(grid[0]) and grid[a][b]=='1' and visited[a][b]==False :
                        arr.append([a,b])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1' and visited[i][j]==False:

                    bfs(i,j)
                    count+=1
        return count
        