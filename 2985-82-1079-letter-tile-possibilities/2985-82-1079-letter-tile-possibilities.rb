# @param {String} tiles
# @return {Integer}
def num_tile_possibilities(tiles)
    poss = []
    perms(tiles).each do |perm|
        (0...perm.length).each do |i|
            poss << perm[0..i]
        end
    end
    poss.uniq.length
end

def perms(string)
    return [string] if string.length < 2
    result = []
    
    char = string[0]
    rest = string[1..-1]
    perms(rest).each do |other_chars|
        (0..other_chars.length).each do |i|
            result << other_chars[0...i] + char + other_chars[i..-1]
        end
    end
    result.uniq
end