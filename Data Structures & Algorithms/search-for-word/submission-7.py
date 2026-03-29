class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        visited = set()
        def bktrak(i,j,strr):
            if strr==word:
                return True
            
            if i<0 or i>=len(board):
                return False
            if j<0 or j>=len(board[0]):
                return False
            if len(strr)>len(word):
                return False
            if (i,j) in visited:
                return False
            else:
                visited.add((i,j))
                for dx,dy in ((1,0),(0,1),(-1,0),(0,-1)):
                    if bktrak(i+dx, j+dy, strr+board[i][j]):
                        return True
                visited.remove((i,j))
                return False


        for i in range(len(board)):
            for j in range(len(board[0])):
                if bktrak(i,j,strr=""):
                    return True
        return False  