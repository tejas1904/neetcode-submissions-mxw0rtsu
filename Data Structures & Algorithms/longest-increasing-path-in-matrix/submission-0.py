class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        def isNotOutOfBounds(x,y):
            if 0<=x and x <len(matrix) and 0<=y and y<len(matrix[0]):
                return True
            else:
                return False
        memo = {}
        def fn(x,y):
            if (x,y) in memo:
                return memo[(x,y)]
            
            longest_len = 1
            for i,j in [(1,0),(-1,0),(0,1),(0,-1)]:
                nx,ny = x+i,y+j
                if isNotOutOfBounds(nx,ny):
                    if matrix[x][y]<matrix[nx][ny]:
                        longest_len = max(longest_len, 1 + fn(nx, ny))
                
            memo[(x,y)] = longest_len
            return memo[(x,y)]
        
        lens= []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                lens.append(fn(i,j))
        return max(lens)
        
        