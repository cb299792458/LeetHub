class MyStack:

    def __init__(self):
        self.a = deque()
        self.b = deque()
        

    def push(self, x: int) -> None:
        if not self.b:
            self.a.append(x)
        else:
            self.b.append(x)

    def pop(self) -> int:
        if not self.b:
            while len(self.a)>1:
                self.b.append(self.a.popleft())
            return self.a.popleft()
        else:
            while len(self.b)>1:
                self.a.append(self.b.popleft())
            return self.b.popleft()
    

    def top(self) -> int:
        if not self.b:
            while len(self.a)>1:
                self.b.append(self.a.popleft())
            res = self.a[0]
            self.b.append(self.a.popleft())
        else:
            while len(self.b)>1:
                self.a.append(self.b.popleft())
            res = self.b[0]
            self.a.append(self.b.popleft())
        
        return res
        

    def empty(self) -> bool:
        return not self.a and not self.b


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()