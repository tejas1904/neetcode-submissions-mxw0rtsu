class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rowdict = defaultdict(set)
        coldict = defaultdict(set)
        boxdict = defaultdict(set)

        for i in range(0,9,1):
            for j in range(0,9,1):
                char = board[i][j]
                if char=='.':
                    continue
                else:
                    if char in rowdict[i]:
                        return False
                    else:
                        rowdict[i].add(char)
                    if char in coldict[j]:
                        return False
                    else:
                        coldict[j].add(char)
                    
                    boxno = (i//3)*3 + (j//3)
                    if char in boxdict[boxno]:
                        return False
                    else:
                        boxdict[boxno].add(char)
        
        return True

        