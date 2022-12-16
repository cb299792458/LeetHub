var uniquePathsWithObstacles = function(obstacleGrid) {
    let row = obstacleGrid.length;
    let col = obstacleGrid[0].length;

    let stepsToEnd = [...Array(row)].map(ele => Array(col).fill(null));

    if(obstacleGrid[row-1][col-1] === 0){
        stepsToEnd[row-1][col-1] = 1;
    } else {
        stepsToEnd[row-1][col-1] = 0;

    }
    

    for (row=obstacleGrid.length-1;row >= 0; row--) {
        for (col=obstacleGrid[0].length-1;col >= 0; col--) {
            if (outOfBounds(obstacleGrid, row, col)) continue;
            let paths = 0;
            if (!outOfBounds(obstacleGrid, row, col + 1)) paths += stepsToEnd[row][col + 1];
            if (!outOfBounds(obstacleGrid, row + 1, col)) paths += stepsToEnd[row + 1][col];
            stepsToEnd[row][col] = stepsToEnd[row][col] || paths;
        }
    }

    return stepsToEnd[0][0];
};

outOfBounds = (obstacleGrid, row, col) => {
    const outOfBoundsRow = row < 0 || row >= obstacleGrid.length;  
    const outOfBoundsCol = col < 0 || col >= obstacleGrid[0].length;
    const rock = obstacleGrid[row] && obstacleGrid[row][col] === 1;

    return outOfBoundsRow || outOfBoundsCol || rock;
}