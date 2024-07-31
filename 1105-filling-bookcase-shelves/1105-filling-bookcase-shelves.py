class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        
        @cache
        def helper(index, width_remaining, current_height):
            if index == len(books):
                return 0
            [width, height] = books[index]
            
            new_shelf = helper(index+1, shelfWidth - width, height) + height
            
            old_shelf = math.inf
            if width_remaining >= width:
                new_height = max(height, current_height)
                increase = max(0, height - current_height)
                old_shelf = helper(index+1, width_remaining - width, new_height) + increase
            
            return min(new_shelf, old_shelf)
        
        return helper(0, shelfWidth, 0)