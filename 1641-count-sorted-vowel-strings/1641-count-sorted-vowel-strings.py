class Solution:
    def countVowelStrings(self, n: int) -> int:
        vowels = ["a","e","i","o","u"]
        endings = {'a':1,'e':1,'i':1,'o':1,'u':1}
        
        for i in range(2,n+1):
            temp = {'a':0,'e':0,'i':0,'o':0,'u':0}
            
            for end in range(5):
                for new in range(end,5):
                    temp[vowels[new]] += endings[vowels[end]]
                    
                
            endings = temp
            
        return sum(endings.values())