class Solution:
    def hammingWeight(self, n: int) -> int:
        count= 0 
        num=n
        while num>0:
            digit = num%2
            if digit==1:
                count+=1
            num=num//2
        return count
        