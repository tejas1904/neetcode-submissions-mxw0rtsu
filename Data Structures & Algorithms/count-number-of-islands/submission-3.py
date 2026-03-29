from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        rows, cols = len(grid), len(grid[0])
        tc = 0

        def isValid(i, j):
            if not (0 <= i < rows and 0 <= j < cols):
                return False
            if grid[i][j] == "0":
                return False
            if (i, j) in visited:
                return False
            return True

        def exploreBFS(i, j):
            queue = deque()
            queue.append((i, j))
            visited.add((i, j))

            while queue:
                x, y = queue.popleft()
                for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                    nx, ny = x + dx, y + dy
                    if isValid(nx, ny):
                        visited.add((nx, ny))
                        queue.append((nx, ny))

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i, j) not in visited:
                    exploreBFS(i, j)
                    tc += 1

        return tc
