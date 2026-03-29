class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dicta = {}

        for num in nums:
            if num not in dicta.keys():
                dicta[num] = 1
            else:
                dicta[num]+=1
        
        counts = [[] for i in range(len(nums)+1)]
        for num in dicta:
            count = dicta[num]
            counts[count].append(num)
        
        result = []
        for i in range(len(counts)-1,-1,-1):
            if len(counts[i])>0:
                result+=(counts[i])
        
        return result[0:k]

        