def num_tile_possibilities(tiles)
    # Count the frequency of each character
    char_counts = Hash.new(0)
    tiles.each_char { |char| char_counts[char] += 1 }
    
    # Start backtracking
    backtrack(char_counts)
end

def backtrack(char_counts)
    total = 0
    
    char_counts.each do |char, count|
        next if count == 0
        
        # Use this character in the current sequence
        total += 1
        char_counts[char] -= 1
        
        # Recurse to build longer sequences
        total += backtrack(char_counts)
        
        # Backtrack: restore the character count
        char_counts[char] += 1
    end
    
    total
end