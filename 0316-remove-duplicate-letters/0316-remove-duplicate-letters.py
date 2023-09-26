class Solution:
    def removeDuplicateLetters(self, s: str) -> str:        
        last_index = defaultdict(int)
        for i,c in enumerate(s):
            last_index[c]=i
        
        seen=set()
        stack=[]
        for i,c in enumerate(s):
            if c in seen: continue
            while stack and ord(stack[-1])>ord(c) and last_index[stack[-1]]>i:
                seen.remove(stack.pop())
            seen.add(c)
            stack.append(c)
        return ''.join(stack)