class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        def climb(n):
            if n>=len(cost):
                return 0
            return cost[n]+min(climb(n+1), climb(n+2))
        
        return min(climb(0),climb(1))
            
            