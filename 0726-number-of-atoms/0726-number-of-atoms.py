class Solution:
    def countOfAtoms(self, formula: str) -> str:
        self.stack = [defaultdict(int)]
        self.element = ''
        self.count = 0
        self.sub = None
        
        def calc():
            if self.sub:
                for ele,cnt in self.sub.items():
                    self.stack[-1][ele] += cnt * (self.count or 1)
            elif self.element:
                self.stack[-1][self.element] += (self.count or 1)
            self.element = ''
            self.count = 0
            self.sub = None
            
        for c in formula:
            if c.isupper():
                calc()
                self.element += c
                
            elif c.islower():
                self.element += c
                
            elif c.isdigit():
                self.count *= 10
                self.count += int(c)
                
            elif c=='(':
                calc()
                self.stack.append(defaultdict(int))
                
            elif c==')':
                calc()
                self.sub = self.stack.pop()
                
        calc()

        assert(len(self.stack)==1)
        items = list(self.stack[-1].items())
        items.sort()
        return ''.join(element + (str(count) if count>1 else '') for element, count in items)