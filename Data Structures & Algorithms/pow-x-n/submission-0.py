class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def mp(x,n):
            if n==1:
                return x
            if n==0:
                return 1
            else:
                if n%2==0:
                    ret = mp(x,n//2)
                    return ret*ret
                else:
                    ret = mp(x,(n-1)//2)
                    return x*ret*ret
        ret =  mp(x,abs(n))
        if n<=0:
            return 1/ret
        else:
            return ret