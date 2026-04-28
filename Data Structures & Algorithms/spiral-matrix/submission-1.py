class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        r,c = len(matrix)-1,len(matrix[0])-1
        visited = set()

        ans = []
        ###############RRR#####DDD######LLL######UUU##
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dfs(x,y,s): 
            ans.append(matrix[x][y])
            visited.add((x,y))
            
            for i in range(4):
                ns = (s+i)%4 
                dx,dy = directions[ns]
                nx,ny = x+dx , y+dy
                if 0 <= nx <= r and 0 <= ny <= c and (nx, ny) not in visited:
                    dfs(nx,ny,ns)
                    return

        dfs(0,0,0)
        return ans

        