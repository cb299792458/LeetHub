/**
 * @param {number[][]} heights
 * @return {number[][]}
 */
var pacificAtlantic = function(heights) {
    
    const maxRow = heights.length-1;
    const maxCol = heights[0].length-1;
    const outOfBounds = (r,c) => {
        return r < 0 || r > maxRow || c < 0 || c > maxCol;
    };
    
    const dirs = [[1,0],[0,1],[-1,0],[0,-1]];
    
    const pSquares = {};
    const aSquares = {};
    
    const dfs = (r,c,memo) => {
        const coords = `${r},${c}`;

        if(memo[coords]) return;
        memo[coords] = true;
        for(let dir of dirs){
            const newRow = r + dir[0];
            const newCol = c + dir[1];
            if(outOfBounds(newRow,newCol)) continue;
            if(heights[r][c] > heights[newRow][newCol]) continue;
            
            dfs(newRow,newCol,memo);
        }
    };
    
    const res = [];
    
    for(let i = 0; i <= maxRow; i++){
        for(let j = 0; j <= maxCol; j++){
            const coords = `${i},${j}`;
            if(i===0 || j===0) dfs(i,j,pSquares);
            if(i===maxRow||j===maxCol) dfs(i,j,aSquares);
        }
    }
    
    for(let i = 0; i <= maxRow; i++){
        for(let j = 0; j <= maxCol; j++){
            const coords = `${i},${j}`;
            
            if(pSquares[coords]===true&&aSquares[coords]===true){
                res.push([i,j]);
            }
        }
    }
        
    return res

}




