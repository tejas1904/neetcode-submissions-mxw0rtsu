class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)-1
        cols = len(board[0])-1

        def dfs(i,j):
            if not(0<=i<=rows) or not(0<=j<=cols):
                return
            if board[i][j]=="X" or board[i][j]=="T":
                return
            #only if its marked as "O"
            board[i][j] = "T"
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
        
        for i in range(rows+1):
            for j in range(cols+1):
                # if (i,j) is a border 
                if (i in (0,rows)) or (j in (0,cols)):
                    if board[i][j]=="O":
                        dfs(i,j)
        
        for i in range(rows+1):
            for j in range(cols+1):
                if board[i][j] == "O":
                    board[i][j] = "X"
        
        for i in range(rows+1):
            for j in range(cols+1):
                if board[i][j] == "T":
                    board[i][j] = "O"

        




            
        