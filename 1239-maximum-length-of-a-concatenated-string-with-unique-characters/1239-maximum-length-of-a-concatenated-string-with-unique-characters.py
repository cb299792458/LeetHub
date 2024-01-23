class Solution:
    def maxLength(self, arr: List[str]) -> int:
        dp = ['']
        for word in arr:
            if len(set(word)) != len(word): continue
            new_dp = []
            for string in dp:
                letters = set(string)
                if not any(c in letters for c in word):
                    new_dp.append(string+word)
                new_dp.append(string)
            dp = new_dp
        
        dp.sort(key=len)
        return len(dp[-1])