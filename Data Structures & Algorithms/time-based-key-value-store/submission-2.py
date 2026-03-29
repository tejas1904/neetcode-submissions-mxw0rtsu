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
        while l<r:
            mid = (l+r)//2
            if target<=arr[mid]:
                r=mid
            else:
                l=mid+1
        mid = l
        if arr[mid] == timestamp:
            return self.dicta[key][arr[mid]]
        elif arr[mid] > timestamp:
            # The lower bound is strictly greater than target,
            # so answer is previous timestamp if it exists
            if mid == 0:
                return ""  # no smaller timestamp available
            else:
                return self.dicta[key][arr[mid - 1]]
        else:
            # arr[mid] < timestamp, so this is the greatest ≤ timestamp
            return self.dicta[key][arr[mid]]
        
