class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dicta={}
        for num in nums:
            if num in dicta:
                dicta[num]+=1
            else:
                dicta[num]=1
        
        cn={}
        for num,count in dicta.items():
            if count in cn:
                cn[count].append(num)
            else:
                cn[count] = [num]
        
        topk = []
        for i in range(len(nums),-1,-1):
            if i in cn:
                topk = topk+cn[i]
        return topk[0:k]
