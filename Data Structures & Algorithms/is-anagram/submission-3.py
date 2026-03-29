class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = defaultdict(int)
        countt = defaultdict(int)

        for letter in s:
            counts[letter] += 1
        for letter in t:
            countt[letter] += 1

        if set(counts.keys())!=set(countt.keys()):
            return False

        for key in counts.keys():
            if counts[key]!=countt[key]:
                return False
        
        return True

