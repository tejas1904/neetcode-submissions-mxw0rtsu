class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        if n==2:
            return 2
        else:
            n_minus_two = 1
            n_minus_one = 2

            for i in range(3,n+1):
                temp = n_minus_two + n_minus_one
                n_minus_two = n_minus_one
                n_minus_one = temp
        
            return n_minus_one
        