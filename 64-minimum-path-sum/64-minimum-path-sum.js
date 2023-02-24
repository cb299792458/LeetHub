var minPathSum = function(grid) {
    let height = grid.length;
    let width = grid[0].length;
    
    let table = new Array(height+1).fill().map(()=> new Array(width+1).fill(Infinity));
    
    table[height-1][width-1] = grid[height-1][width-1];
    // console.log(table);
    
    for(let row=height-1;row>=0;row--){
        for( let col=width-1;col>=0;col--){
            if(row===height-1 && col===width-1) continue;
            table[row][col] = grid[row][col] + Math.min(table[row+1][col],table[row][col+1]);
        }
    }

    // console.log(table);
    return table[0][0];
};