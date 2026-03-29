class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        hashset = {}
        ans=[]
        for i in range(len(nums)):
            for j in range(len(nums)):
                for k in range(len(nums)):
                    if(i==j or j==k or k==i):
                        continue
                    else:
                        numarr = [nums[i],nums[j],nums[k]]
                        ans.append(numarr)
                        if sum(numarr)==0:
                            hashset[tuple(sorted(numarr))]=0
        return [list(key) for key in hashset]