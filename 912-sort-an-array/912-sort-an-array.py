class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        return nums
        # quicksort
#         if len(nums) < 2: return nums
        
#         pivot = nums[len(nums)//2]
#         left = [x for x in nums if x < pivot]
#         mid = [y for y in nums if y == pivot]
#         right = [z for z in nums if z > pivot]
        
#         return self.sortArray(left) + mid + self.sortArray(right)

        # mergesort
        
#         if len(nums) < 2: return nums
#         left = nums[:len(nums)//2]
#         right = nums[len(nums)//2:]
        
#         left = self.sortArray(left)
#         right = self.sortArray(right)
        
#         return merge(left,right)
    
#     def merge(left,right):
#         ans = []
#         while len(left) and len(right):
#             if(left[0] < right[0]):
#                 ans.append(left.pop())
#             else:
#                 ans.append(right.pop())
#         return ans + left + right