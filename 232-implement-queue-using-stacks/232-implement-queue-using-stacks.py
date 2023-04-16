class MyQueue:

    def __init__(self):
        self.input=[]
        self.output=[]

    def push(self, x: int) -> None:
        self.input.append(x)

    def pop(self) -> int:
        self._stack_to_queue()
        return self.output.pop()

    def peek(self) -> int:
        self._stack_to_queue()
        return self.output[-1]

    def empty(self) -> bool:
        return False if self.input or self.output else True
        
    def _stack_to_queue(self):
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()