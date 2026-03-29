class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def isPali(strr):
            i, j = 0, len(strr) - 1
            while i <= j:
                if strr[i] != strr[j]:
                    return False
                i,j = i+1,j-1
                
            return True
        
        ans = []
        arr = []
        def bktrak(start):
            if start==len(s):
                ans.append(arr.copy())
            else:
                for i in range(start,len(s)):
                    possible_start_str = s[start:i+1]
                    if isPali(possible_start_str):
                        arr.append(possible_start_str)
                        bktrak(i+1)
                        arr.pop(-1)
        bktrak(0)
        return ans
