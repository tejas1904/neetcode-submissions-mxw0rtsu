class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        
        num = n
        while True:
            summ = 0 
            while num>0:
                digit = num%10
                summ+=digit**2
                num=int(num/10)
            if summ in seen:
                return False
            elif summ==1:
                return True
            
            seen.add(summ)
            num = summ
            

        