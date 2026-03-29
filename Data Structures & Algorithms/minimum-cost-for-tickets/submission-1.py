class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        memo ={}
        def fn(i):
            if i in memo:
                return memo[i]
            
            elif i==len(days):
                return 0
            
            else:

                #buy 1 day pass
                j = i
                last_day_of_pass = days[i]+1-1
                
                while j<len(days) and days[j]<= last_day_of_pass:
                    j+=1
                
                costa = costs[0] + fn(j)

                #buy 7 day pass
                j = i
                last_day_of_pass = days[i]+7-1
                
                while j<len(days) and days[j]<= last_day_of_pass:
                    j+=1
                
                costb = costs[1] + fn(j)

                #buy 30 day pass
                j = i
                last_day_of_pass = days[i]+30-1
                
                while j<len(days) and days[j]<= last_day_of_pass:
                    j+=1
                
                costc = costs[2] + fn(j)


                memo[i] =  min(costa,costb,costc)
                return memo[i]
        
        return fn(0)
        