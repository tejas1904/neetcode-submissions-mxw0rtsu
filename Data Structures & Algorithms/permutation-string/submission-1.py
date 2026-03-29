class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hm1 = defaultdict(int)
        for char in s1:
            hm1[char]+=1
        
        hm2 = defaultdict(int)
        for char in s2[0:len(s1)]:
            hm2[char]+=1
        i=0
        j=len(s1)
        while j<len(s2):
            if hm1==hm2:
                return True
            hm2[s2[i]]-=1
            if hm2[s2[i]]==0:
                del hm2[s2[i]]
            i+=1
            hm2[s2[j]]+=1
            j+=1
        return hm1 == hm2


        