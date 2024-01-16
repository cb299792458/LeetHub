class RandomizedSet:

    def __init__(self):
        self.list = list()
        self.indices = dict()
        

    def insert(self, val: int) -> bool:
        if val in self.indices:
            return False
        
        self.list.append(val)
        self.indices[val] = len(self.list)-1
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.indices:
            return False
        i = self.indices[val]

        self.list[i],self.list[-1] = self.list[-1],self.list[i]
        self.indices[self.list[i]] = i

        del self.indices[self.list.pop()]
        return True
        

    def getRandom(self) -> int:
        return random.choice(self.list)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()