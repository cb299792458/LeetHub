var updateMatrix = function(mat) {
    const queue = [];

    const res = [];
    res.push(new Array(mat.length))
    for (let row = 0; row < mat.length; row++){
        res[row] = new Array(mat[0].length)
        for (let col = 0; col < mat[0].length; col++){
            
            if (mat[row][col] === 0) {
                res[row][col] = 0;
                queue.push([row, col, 0])
            }
        }
    }

    let directions = [[1,0], [0,1], [-1,0], [0,-1]]
    while (queue.length > 0) {
        const [row, col, level] = queue.shift();

        if (inBounds(mat, row, col)) {

            for (let dir of directions) {
                const newRow = row + dir[0];
                const newCol = col + dir[1];
                if (inBounds(mat, newRow, newCol) && res[newRow][newCol] === undefined) {
                    queue.push([newRow, newCol, level+1])
                    res[newRow][newCol] = level+1
                }
            }
        }
    }

    return res
};

const inBounds = (grid, row, col) => {
    const rowInBounds = 0 <= row && row < grid.length;
    const colInBounds = 0 <= col && col < grid[0].length;
    return rowInBounds && colInBounds
}

