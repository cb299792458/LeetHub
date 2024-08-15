class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        register = defaultdict(int)
        for bill in bills:
            match bill:
                case 5:
                    register[5] += 1
                case 10:
                    if register[5]:
                        register[5] -= 1
                        register[10] += 1
                    else:
                        return False
                case 20:
                    if register[10] and register[5]:
                        register[10] -= 1
                        register[5] -= 1
                    elif register[5]>=3:
                        register[5] -= 3
                    else:
                        return False
        return True
                        