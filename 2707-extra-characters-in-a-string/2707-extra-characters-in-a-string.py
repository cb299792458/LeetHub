class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dp = [0] + [float('inf')] * len(s)
        
        for i in range(len(s)+1):
            dp[i]=min(dp[i],dp[i-1]+1)
            for word in dictionary:
                if word==s[i:i+len(word)]:
                    print(word,s[i:i+len(word)], i)
                    dp[i+len(word)] = min(dp[i],dp[i+len(word)])
        
        print(dp)
        return dp[-1]