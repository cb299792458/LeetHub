class Solution:
    def minOperations(self, logs: List[str]) -> int:
        ops = 0
        for log in logs:
            match log:
                case './':
                    pass
                case '../':
                    if ops:
                        ops -= 1
                case _:
                    ops += 1
        return ops