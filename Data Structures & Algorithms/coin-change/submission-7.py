class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        memo = {}
        def fn(capacity):
            if capacity in memo:
                return memo[capacity]
            if capacity==amount:
                return 0
            if capacity>amount:
                return float('inf')
            ret = float('inf')
            for coin in coins:
                ret = min(fn(capacity+coin),ret)

            memo[capacity] = 1+ ret
            return memo[capacity]
        
        ans =  fn(0)
        if ans==float('inf'):
            return -1
        else:
            return ans