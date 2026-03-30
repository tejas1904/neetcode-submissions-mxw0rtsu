import functools
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows=len(matrix)
        cols=len(matrix[0])
        visited = {}
        
        @functools.lru_cache(None)
        def exploreFrom(i,j):
            maxlen = 1
            for dx,dy in ((1,0),(0,1),(-1,0),(0,-1)):
                nx,ny = i+dx , j+dy
                
                if 0<=nx and nx<=rows-1 and 0<=ny and ny<=cols-1:
                    if matrix[i][j]<matrix[nx][ny]:
                        leng = 1+exploreFrom(nx,ny)
                        maxlen = max(maxlen,leng)
                
            return maxlen
        
        lens = []
        for i in range(rows):
            for j in range(cols):
                lens.append(exploreFrom(i,j))
        return max(lens)

        