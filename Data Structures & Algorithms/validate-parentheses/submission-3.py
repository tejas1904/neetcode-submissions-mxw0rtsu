class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hm = {"}":"{",")":"(","]":"["}
        for char in s:
            if char in hm.keys():
                if len(stack)<=0:
                    return False
                if stack.pop(-1) != hm[char]:
                    return False
            else:
                stack.append(char)
        
        if len(stack)>0:
            return False
        else:
            return True
