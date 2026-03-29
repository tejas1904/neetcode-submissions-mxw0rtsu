class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def twoSum(num,arr):
            target = 0-num
            if len(arr)<2:
                return []

            l=0
            r=len(arr)-1
            ans = []
            while l<r:
                Sum = arr[l]+arr[r]
                if Sum==target: # find all pairs that equal target
                    ans.append([num,arr[l],arr[r]])
                    l+=1
                    r-=1
                elif Sum>target:
                    r=r-1
                else:
                    l=l+1
            return ans
        def sort3(arr):
            a,b,c = arr[0],arr[1],arr[2]
            if b<a:
                a,b = b,a
            if c<b:
                if c<a:
                    a,b,c = c,a,b
                if c<b:
                    a,b,c = a,c,b
            return [a,b,c]

        
        nums = sorted(nums) ## sort
        ans=[]
        i=0
        for i in range(len(nums)):
            ret = twoSum(num = nums[i] ,arr=nums[i+1:]) # for each number find the sum pairs in the next part of arr
            if len(ret)>0:
                ans+=ret
        
        ansset=set()
        for triplet in ans:
            ansset.add(tuple(sort3(triplet)))

        return [list(item) for item in ansset]
         