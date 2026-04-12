class Solution:
    def checkValidString(self, s: str) -> bool:
        openStack = []
        starStack = []

        for i in range(len(s)):
            char = s[i]

            if char == '(':
                openStack.append(i)
            elif char == '*':
                starStack.append(i)
            elif char == ')':
                if openStack:
                    openStack.pop()     # use top of stack
                elif starStack:
                    starStack.pop()     # use top of stack
                else:
                    return False

    

        while openStack and starStack:
            i1 = openStack.pop()
            i2 = starStack.pop()

            if i1 < i2:
                pass
            else:
                return False

        return len(openStack) == 0