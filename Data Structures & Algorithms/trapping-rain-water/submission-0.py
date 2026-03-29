class Solution:
    def trap(self, height: List[int]) -> int:

        cachement = [0 for _ in range(len(height))]
        
        for pos in range(len(height)):
            if height[pos]>0:
                #pos=8
                low = 0
                high = len(height)-1

                p1 = pos
                p2 = pos

                i=pos-1
                while i>=low:
                    if height[i]>=height[pos]:
                        p1 = i
                        break
                    i=i-1
                i= pos+1
                while i<=high:
                    if height[i]>=height[pos]:
                        p2 = i
                        break
                    i=i+1

                if p1!=p2:
                    for i in range(p1+1,p2):
                        cachement[i] = 1 

        print(cachement)
        totalArea = 0
        i=0
        while i<len(cachement):
            if cachement[i]==1:
                l=i-1
                width = 0
                bricksInCachement = 0
                while cachement[i]==1:
                    width += 1
                    bricksInCachement += height[i]
                    i+=1
                r=i
                print(l,r,width,bricksInCachement)
                totalArea = totalArea + (min(height[r],height[l])*width)-bricksInCachement

            i+=1

        print(totalArea)
        return totalArea
