class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=deque()
        for asteroid in asteroids:
            stack.append(asteroid)
            
            while len(stack)>1 and stack[-2]>0 and stack[-1]<0:
                right=stack.pop()
                left=stack.pop()
                
                if -right>left:
                    stack.append(right)
                elif -right<left:
                    stack.append(left)
        return stack