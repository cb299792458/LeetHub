class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [[position[i],speed[i],(target-position[i])/speed[i]] for i in range(len(position))]
        cars.sort(key=lambda x: x[0], reverse=False)
               
        fleets=0
        stack=deque([cars.pop()])
        
        while cars:
            new_car = cars.pop()
            last_car = stack[-1]
            
            if last_car[2] < new_car[2]:
                stack.append(new_car)
        
        return len(stack)