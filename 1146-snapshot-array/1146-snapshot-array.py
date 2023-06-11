class SnapshotArray:

    def __init__(self, length: int):
        self.history={}
        self.snap_id=0
        self.array=[[[0,0]] for _ in range(length)]

    def set(self, index: int, val: int) -> None:
        self.array[index].append([self.snap_id,val])

    def snap(self) -> int:
        self.snap_id+=1
        return self.snap_id-1

    def get(self, index: int, snap_id: int) -> int:
        timeline = self.array[index]
        l,r=0,len(timeline)-1
        
        while l<r:
            m=(l+r+1)//2
            if timeline[m][0]<=snap_id:
                l=m
            else: r=m-1
        return timeline[l][1]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)