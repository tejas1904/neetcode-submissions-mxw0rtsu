class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zr = set()
        zc = set()

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c]==0:
                    zr.add(r)
                    zc.add(c)

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if (r in zr) or (c in zc):
                    matrix[r][c]=0
        
        

        