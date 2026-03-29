class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)

        result = set()
        for i in range(len(nums)):
            l = 0
            if l==i:
                l+=1
            h = len(nums)-1
            if h==i:
                h=h-1
            while l<h:
                target = nums[i] * -1
                summ = nums[l]+nums[h]

                if summ==target:
                    result.add(tuple(sorted([nums[i],nums[l],nums[h]])))
                    l += 1
                    if l==i:
                        l+=1
                    h -= 1
                    if h==i:
                        h=h-1
                elif summ<target:
                    l = l+1
                    if l==i:
                        l+=1
                elif summ>target:
                    h = h-1
                    if h==i:
                        h=h-1 
        return [list(x) for x in result]   