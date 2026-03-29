class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def isPalindrome(s):
            l,r = 0,len(s)-1
            while l<=r and s[l]==s[r]:
                l = l+1
                r = r-1
            if l>r:
                return True
            else:
                return False
            
        ans = []
        arr = []
        def bktrak(start):
            if start==len(s):
                ans.append(arr.copy())
                return
            else:
                possible_start_str = ""
                for i in range(start , len(s)):
                    possible_start_str += s[i]
                    if isPalindrome(possible_start_str):
                        arr.append(possible_start_str)
                        bktrak(i+1)
                        arr.pop()
        
        bktrak(0)
        return ans

                


        