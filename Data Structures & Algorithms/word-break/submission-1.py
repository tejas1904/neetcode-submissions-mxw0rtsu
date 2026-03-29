class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        memo = {}

        def fn(s):
            if s=='':
                return True
            if s in memo:
                return memo[s]
            
            for word in wordDict:
                i,j= 0,len(word)
                if s[i:j]==word:
                    ret =  fn(s[j:])
                    if ret:
                        memo[s] = True
                        return memo[s]
            memo[s] = False
            return memo[s]
        
        return fn(s)


        