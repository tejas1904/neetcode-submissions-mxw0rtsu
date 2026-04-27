class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        
        num = n
        while True:
            thisnum = num
            summ = 0 
            while thisnum>0:
                digit = thisnum%10
                summ+=digit**2
                thisnum=int(thisnum/10)
            if summ in seen:
                return False
            elif summ==1:
                return True
            
            seen.add(summ)
            num = summ
            

        