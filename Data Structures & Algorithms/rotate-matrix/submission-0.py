class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n=len(matrix)

        i,j=0,len(matrix)-1
        while i<j:
            temp = matrix[i]
            matrix[i] = matrix[j]
            matrix[j] = temp
            i+=1
            j-=1
        
        for diagonal in range(0,n):
            r,c = diagonal,diagonal
            for di in range(r+1,n):
                matrix[r][di],matrix[di][c] = matrix[di][c],matrix[r][di]
        

        


        

        
        