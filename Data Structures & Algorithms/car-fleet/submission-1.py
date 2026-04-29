class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #if  no cars then just return zero 
        if len(position)==0:
            return 0
        
        cars = []
        for position,speed in zip(position,speed):
            cars.append([position,speed])
        
        #sorting : where the car nearest position to the target is at the begening of the array
        cars.sort(reverse=True)

        fleet=1
        pos,spd = cars[0]
        nearestFleetReachTime=(target-pos)/spd
        
        for pos,spd in cars[1:]:
            timeToReach = (target-pos)/spd
            #car is blocked by the fleet,it becomes part of the fleet
            if timeToReach<=nearestFleetReachTime:
                pass
            # if then car is not blocked it creates a new fleet
            else:
                fleet+=1
                nearestFleetReachTime = timeToReach
        
        return fleet