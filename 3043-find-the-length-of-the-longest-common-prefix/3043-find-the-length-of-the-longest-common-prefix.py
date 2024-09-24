class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        arr1 = [str(n) for n in arr1]
        arr2 = [str(n) for n in arr2]
        prefixes = set()
        for word in arr1:
            for i in range(1,len(word)+1):
                prefixes.add(word[:i])
        
        result = 0
        for word in arr2:
            for i in range(1,len(word)+1):
                if word[:i] in prefixes:
                    result = max(result, len(word[:i]))
        
        return result