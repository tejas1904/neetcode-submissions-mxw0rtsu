class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hset = set(nums)
        visited = set()
        maxstreak = 0
        i = 0
        for i in range(len(nums)):
            number = nums[i]
            if number not in visited:
                visited.add(number)
                if number-1 not in hset:
                    streak = 1
                    while number+1 in hset:
                        streak +=1
                        visited.add(number+1)
                        number = number+1
                    maxstreak = max(streak,maxstreak)
        return maxstreak


