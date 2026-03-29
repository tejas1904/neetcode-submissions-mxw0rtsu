class Solution:
    def change(self, target: int, coins: List[int]) -> int:
        memo = {}
        def dp(start,curr_summ):
            if (start,curr_summ) in memo:
                return memo[(start,curr_summ)]
            if curr_summ==target:
                return 1
            if curr_summ>target:
                return 0
            if start==len(coins):
                return 0
            else:
                ret = []
                for x in range(start,len(coins)):
                    ret.append(dp(x,curr_summ+coins[x]))
                memo[(start,curr_summ)] =  sum(ret)
                return memo[(start,curr_summ)]
        
        return dp(0,0)
        