/**
 * @param {character[][]} grid
 * @return {number}
 */
var numIslands = function(grid) {
    function fillIsland(row,col){
        if(row<0 || row===grid.length) return;
        if(col<0 || col===grid[0].length) return;
        if(grid[row][col] === '0') return;
        grid[row][col] = '0';
        fillIsland(row+1,col);
        fillIsland(row,col+1);
        fillIsland(row-1,col);
        fillIsland(row,col-1);
    }
    let count = 0;
    for(let row = 0; row < grid.length; row++){
        for(let col = 0; col < grid[0].length; col++){
            if(grid[row][col] === '1'){
                count++;
                fillIsland(row,col);
            }
        }
    }
    return count;
};