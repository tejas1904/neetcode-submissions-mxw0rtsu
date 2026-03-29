class TimeMap:

    def __init__(self):
        self.dicta = {}
        self.tsdicta = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        
        if key not in self.dicta.keys():
            self.dicta[key] = {}
            self.tsdicta[key]= []
        
        self.dicta[key][timestamp] = value
        self.tsdicta[key].append(timestamp)
            
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.tsdicta:
            return ""

        arr = self.tsdicta[key]
        target = timestamp
        
        l=0
        r=len(arr)-1

        lastConditionMetIndex=None
        while l<=r:
            mid = (l+r)//2
            if arr[mid]<=timestamp: #if condition met look forward , 
            #but make note as this might be the last time you see a good condition
                lastConditionMetIndex = mid
                l=mid+1
            else:#if condition is not met then look behind
                r=mid-1
        
        if lastConditionMetIndex!=None and arr[lastConditionMetIndex]<=timestamp:
            return self.dicta[key][arr[lastConditionMetIndex]]
        else:
            return ""

        
