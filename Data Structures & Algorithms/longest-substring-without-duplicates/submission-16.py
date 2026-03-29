class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        maxlen=1
        currset = set()
        i=0
        j=0
        currset.add(s[i])
        while i<=j and j<=len(s)-2:
            while s[j+1] in currset:
                currset.remove(s[i])
                i+=1
            
            j+=1
            currset.add(s[j])
            maxlen = max(j-i+1 , maxlen)
        
        return maxlen

                
        