class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        skip = set()
        
        changed = True
        while changed:
            changed = False
            
            for i in range(len(accounts)):
                if i in skip:
                    continue
                name = accounts[i][0]
                emails = accounts[i][1:]
                
                
                for j in range(1,len(accounts[i])):
                    email = accounts[i][j]
                    
                    for k in range(i+1,len(accounts)):
                        if k in skip:
                            continue
                        if email in accounts[k]:
                            changed = True
                            skip.add(k)
                            
                            emails += accounts[k][1:]
                emails = list(set(emails))
                emails.sort()
                            
                accounts[i] = [name] + emails
                

            
        return [accounts[i] for i in range(0,len(accounts)) if i not in skip]