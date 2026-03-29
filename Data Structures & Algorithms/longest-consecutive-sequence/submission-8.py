class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        visited = {num: False for num in nums}
        maxval = 0

        for num in nums:
            # only start from numbers that are sequence starts
            if num - 1 not in visited:
                length = 1
                tnum = num + 1
                while tnum in visited:
                    visited[tnum] = True
                    length += 1
                    tnum += 1
                maxval = max(maxval, length)
        
        return maxval
