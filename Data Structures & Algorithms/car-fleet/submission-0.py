class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = []
        cars = []
        for i in range(len(position)):
            time = (target-position[i])/speed[i]
            cars.append((position[i],time))
            
        cars.sort(key=lambda x:x[0], reverse = True)

        fleet = 0
        curr_fleet_time = 0

        for p,t in cars:
            if t > curr_fleet_time:
                fleet+=1
                curr_fleet_time = t

        return fleet
            
            



        




        