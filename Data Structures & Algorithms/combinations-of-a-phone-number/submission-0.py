class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits)==0:
            return []
        ans = []
        digits = list(digits)
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(i,currstring):
            if i>=len(digits):
                ans.append(currstring)
                return
            
            for char in digitToChar[digits[i]]:
                newstring = currstring+char
                backtrack(i+1,newstring)

        
        backtrack(0,"")
        return ans
