class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for p,s in zip(position,speed):
            cars.append([p,s])
        
        cars = sorted(cars,reverse=True)
        stack = []
        for p,s in cars:
            timeToFinish = (target-p)/s
            if len(stack)>0:
                if timeToFinish<=stack[-1]:
                    pass
                else:
                    stack.append(timeToFinish)
            else:
                stack.append(timeToFinish)
        return len(stack)




        