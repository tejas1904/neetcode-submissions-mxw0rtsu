class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1dict = {}
        windowdict = {}
        for i in range(ord('a'), ord('z') + 1):
            s1dict[chr(i)] = 0
            windowdict[chr(i)] = 0

        for i in range(len(s1)):
            s1dict[s1[i]] += 1
            windowdict[s2[i]] += 1
        
        matches = 0
        for key in windowdict:
            if s1dict[key] == windowdict[key]:
                matches += 1
        
        if matches == 26:
            return True
        
        i = 0
        j = len(s1)

        while j < len(s2):
            char_i = s2[i]
            previouslyMatching = (windowdict[char_i] == s1dict[char_i])
            windowdict[char_i] -= 1
            newMatching = (windowdict[char_i] == s1dict[char_i])
            if not previouslyMatching and newMatching:
                matches += 1
            if previouslyMatching and not newMatching:
                matches -= 1
            
            i += 1
            
            # ---- FIXED: use j BEFORE incrementing it ----
            char_j = s2[j]
            previouslyMatching = (windowdict[char_j] == s1dict[char_j])
            windowdict[char_j] += 1
            newMatching = (windowdict[char_j] == s1dict[char_j])
            if not previouslyMatching and newMatching:
                matches += 1
            if previouslyMatching and not newMatching:
                matches -= 1

            if matches == 26:
                return True
            
            j += 1  # moved to end
        
        return False
