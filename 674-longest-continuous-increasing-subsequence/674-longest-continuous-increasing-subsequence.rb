# @param {Integer[]} nums
# @return {Integer}
def find_length_of_lcis(nums)
    length = 1
    max_length = 1
    nums.each_with_index do |num,i|
        next if i == 0
        if num > nums[i-1]
            length += 1
            max_length = length if length > max_length
        else
            length = 1
        end
    end
    max_length
        
end