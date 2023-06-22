class Solution:
    def defangIPaddr(self, address: str) -> str:
        return ''.join([c if c!='.' else '[.]' for c in address ])