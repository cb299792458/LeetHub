# @param {Integer[][]} grid
# @return {Integer}
def max_increase_keeping_skyline(grid)
    row_maxes = []
    col_maxes = []
    grid.each_with_index do |row,index|
        row_maxes[index] = row.max
    end
    grid.transpose.each_with_index do |col,index|
        col_maxes[index] = col.max
    end
    
    n = grid.length
    answer = 0
    
    new_grid = Array.new(n) {Array.new(n)}
    (0...n).each do |r|
        (0...n).each do |c|
            new_grid[r][c] = [row_maxes[r],col_maxes[c]].min
            answer += new_grid[r][c] - grid[r][c]
        end
    end
    answer
end