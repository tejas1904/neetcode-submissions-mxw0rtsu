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

        lastConditionMetIndex = None

        while l <= r:
            mid = (l + r) // 2
            if arr[mid] <= timestamp:
                lastConditionMetIndex = mid
                l = mid + 1
            else:
                r = mid - 1

        if lastConditionMetIndex is not None:
            return self.dicta[key][arr[lastConditionMetIndex]]
        else:
            return ""

        
