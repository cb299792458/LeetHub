class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k>=len(arr):
            return max(arr)
        
        arr = deque(arr)
        wins = 0
        
        while wins<k:
            a=arr.popleft()
            b=arr.popleft()
            if a>b:
                wins+=1
                arr.appendleft(a)
                arr.append(b)
            else:
                wins=1
                arr.appendleft(b)
                arr.append(a)
        
        return arr[0]