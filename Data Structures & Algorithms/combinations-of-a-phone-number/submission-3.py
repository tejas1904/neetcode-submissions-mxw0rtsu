class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digits = [int(digit) for digit in digits]
        if len(digits)==0:
            return []

        charset = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz"
        }

        ans = []
        def bktrak(i,currStr):
            if i==len(digits):
                ans.append(currStr)
            else:
                for char in charset[digits[i]]:
                    
                    bktrak(i+1, currStr+char)
        bktrak(0,"")
        return ans