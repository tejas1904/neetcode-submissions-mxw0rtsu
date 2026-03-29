class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        len1=len(s)
        len2=len(t)
        dict1={}
        dict2={}
        if len1!=len2:
            return False
        for char in s:
            if char not in dict1.keys():
                dict1[char]=0;
            else:
                dict1[char]+=1;
        
        for char in t:
            if char not in dict2.keys():
                dict2[char]=0;
            else:
                dict2[char]+=1;
        
        return dict1==dict2
        