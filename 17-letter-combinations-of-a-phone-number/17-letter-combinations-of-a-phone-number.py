class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res = ['']
        letters = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        
        for num in digits:
            temp = []
            for string in res:
                for char in letters[num]:
                    temp.append(string+char)
            res = temp
        return res
                    