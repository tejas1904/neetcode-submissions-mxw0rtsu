class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        i=0
        j=len(nums)-1

        dicta = {}

        def HR(i,j):
            if (i, j) in dicta:
                return dicta[(i, j)]
            elif i==j:
                dicta[(i, j)] =  nums[i]
                return dicta[(i, j)]
            elif (j-i)==1:
                dicta[(i, j)] = max(nums[i],nums[j])
                return dicta[(i, j)]
            else:
                dicta[(i, j)] =  max(nums[i]+HR(i+2,j) , HR(i+1,j))
                return dicta[(i, j)]
        
        return HR(i,j)

        