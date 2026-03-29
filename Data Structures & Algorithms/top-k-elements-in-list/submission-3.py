class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqdict={}
        for num in nums:
            freqdict[num] = freqdict.get(num,0) + 1
        
        bucketDict = defaultdict(list)
        for number,freq in freqdict.items():
            bucketDict[freq].append(number)
        
        result = []
        for key in sorted(bucketDict,reverse=True):
            result+=bucketDict[key]
        
        return result[:k]
        


