class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        n = len(letters)
        left, right = 0, n - 1
        result = letters[0]  # Initialize result with the first letter as the default value

        while left <= right:
            mid = left + (right - left) // 2

            if letters[mid] <= target:
                left = mid + 1
            else:
                result = letters[mid]
                right = mid - 1

        return result