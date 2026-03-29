 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies  ={}

        for num in nums:
            if num in frequencies.keys():
                frequencies[num]+=1
            else:
                frequencies[num]=1
        
        max_freq = -1
        count_to_list = {}
        for num in frequencies.keys():
            freq = frequencies[num]
            max_freq = max(freq,max_freq)
            try:
                count_to_list[freq].append(num)
            except:
                count_to_list[freq] = [num]
        
        return_arr = []
        while len(return_arr)<k:
            try:
                return_arr.extend(count_to_list[max_freq])
            except:
                pass  
            max_freq -= 1
        
        return return_arr



        