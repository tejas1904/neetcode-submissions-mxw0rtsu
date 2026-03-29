class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def number_of_ways_to_stair(n):
            if n==1:
                return 1 
            if n==2:
                return 2
            if n in memo:
                return memo[n]
            
            memo[n] = (number_of_ways_to_stair(n-1)+
            number_of_ways_to_stair(n-2))
            return memo[n]
        
        return number_of_ways_to_stair(n)
            
        