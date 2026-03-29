class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ans = []
        arr = []

        def bktrak(i):
            if i == len(nums):
                ans.append(arr.copy())
            else:
                #choose
                arr.append(nums[i])
                bktrak(i+1)
                arr.pop(-1)

                #not choose (move the not choose ptr to the next elemt at end of sequence)
                j=i+1
                while j<len(nums) and nums[i]==nums[j]:
                    i+=1
                    j+=1

                bktrak(i+1)
                
        bktrak(0)
        return ans




            