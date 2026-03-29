class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        arr = []
        for char in s:
            if ord('a')<=ord(char)<=ord('z') or ord('0')<=ord(char)<=ord('9'):
                arr.append(char)
        s=arr.copy()
        
        l=0
        r=len(s)-1

        while l<r:
            if s[l]!=s[r]:
                return False
            l+=1
            r-=1
        return True