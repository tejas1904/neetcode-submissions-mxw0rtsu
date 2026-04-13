class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastOccuranceOf = {}
        for i in range(len(s)):
            char = s[i]
            lastOccuranceOf[char] = i
        
        start=0
        furtestPartitionPoint = 0
        ans = []
        for i in range(len(s)):
            char = s[i]
            furtestPartitionPoint = max(furtestPartitionPoint,lastOccuranceOf[char])
            if i==furtestPartitionPoint:
                ans.append(i-start+1)
                start=i+1

        return ans


        