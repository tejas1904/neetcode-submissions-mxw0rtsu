class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        for center in range(len(s)):
            i,j = center,center

            while 0<=i and j<=len(s)-1:
                if s[i]==s[j]:
                    count+=1
                    i=i-1
                    j=j+1
                else:
                    break
            
            i,j = center,center+1

            while 0<=i and j<=len(s)-1:
                if s[i]==s[j]:
                    count+=1
                    i=i-1
                    j=j+1
                else:
                    break
        return count