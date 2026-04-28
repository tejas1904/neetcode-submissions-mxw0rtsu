class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n, m = len(matrix) - 1, len(matrix[0]) - 1
        visited = set()
        ans = []

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dfs(x, y, s):
            ans.append(matrix[x][y])
            visited.add((x, y))

            for turn in range(4):
                ns = (s + turn) % 4
                dx, dy = directions[ns]
                nx, ny = x + dx, y + dy

                if 0 <= nx <= n and 0 <= ny <= m and (nx, ny) not in visited:
                    dfs(nx, ny, ns)
                    return

        dfs(0, 0, 0)
        return ans