from collections import deque
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        pushed = deque(pushed)
        popped = deque(popped)
        
        while pushed or popped:
            # print(stack,pushed,popped)
            if stack and popped and stack[-1]==popped[0]:
                popped.popleft()
                stack.pop()
            elif pushed:
                stack.append(pushed.popleft())
            else:
                return False
                
        # print(pushed,popped)
        
        return True
        
        