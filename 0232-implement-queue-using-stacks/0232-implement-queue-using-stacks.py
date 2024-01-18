class MyQueue:

    def __init__(self):
        self.input = []
        self.out = []

        
    def push(self, x: int) -> None:
        self.input.append(x)

    def pop(self) -> int:
        self._refill()
        return self.out.pop()

    def peek(self) -> int:
        self._refill()
        return self.out[-1]

    def empty(self) -> bool:
        return not self.input and not self.out
        
    def _refill(self):
        if len(self.out) == 0:
            while len(self.input) > 0:
                self.out.append(self.input.pop())

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()