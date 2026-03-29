class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        ans = []

        def backtrack(strp,count_open,count_close):
            if count_close>count_open:
                return
            if len(strp)==2*n:
                if count_close==count_open:
                    ans.append(strp)
                return
            
            
            backtrack(strp+"(" ,count_open+1, count_close)
        
            backtrack(strp+")" ,count_open, count_close+1)



        backtrack("",0,0)
        return ans
        