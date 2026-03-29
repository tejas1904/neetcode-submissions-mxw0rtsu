class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        def backtrack(i,j,k):
            if i<0 or len(board)-1<i:
                return False
            if j<0 or len(board[0])-1<j:
                return False
            if k>=len(word):
                return False
            if (i,j) in visited:
                return False

            if board[i][j] == word[k]:
                if k==len(word)-1:
                    return True
                else:
                    visited.add((i,j))
                    ret_explore = backtrack(i,j+1,k+1) or backtrack(i,j-1,k+1) or backtrack(i+1,j,k+1) or backtrack(i-1,j,k+1)
                    visited.remove((i,j))
                    return True and ret_explore
            else:
                return False
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(i,j,0):
                    return True
        
        return False

        