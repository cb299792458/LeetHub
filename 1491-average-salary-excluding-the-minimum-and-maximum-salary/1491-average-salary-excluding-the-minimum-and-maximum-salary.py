class Solution:
    def average(self, salary: List[int]) -> float:
        # salary.sort()
        # return sum(salary[1:-1])/(len(salary)-2)
    
        big = float('-inf')
        small = float('inf')
        sum=0
        
        for sal in salary:
            sum+=sal
            big=max(sal,big)
            small=min(sal,small)
            
        sum -= big+small
        return sum/(len(salary)-2)
        