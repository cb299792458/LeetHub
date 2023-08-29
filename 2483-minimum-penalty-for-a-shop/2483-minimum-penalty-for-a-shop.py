class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n=len(customers)
        o_pen=[]
        c_pen=[]
        
        n_so_far = 0
        y_to_come = len([c for c in customers if c=='Y'])
        
        for c in customers:
            o_pen.append(n_so_far)
            c_pen.append(y_to_come)
            
            if c=='Y':
                y_to_come-=1
            else:
                n_so_far+=1
        
        o_pen.append(n_so_far)
        c_pen.append(y_to_come)
        
        best = None
        lowest = float('inf')

        for (i,(o,c)) in enumerate(zip(o_pen,c_pen)):
            if o+c<lowest:
                best = i
            lowest = min(o+c,lowest)
            
        return best