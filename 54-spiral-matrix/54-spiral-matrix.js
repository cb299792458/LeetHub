/**
 * @param {number[][]} matrix
 * @return {number[]}
 */
var spiralOrder = function(matrix) {
    const dirs = [[0,1],[1,0],[0,-1],[-1,0]];
    let dirIdx = 0;
    const rows = matrix.length;
    const cols = matrix[0].length;
    
    // Set up boundary around matrix
    let out = new Set;
    for(let i = -1; i <= rows; i ++){
        for(let j = -1; j <= cols; j ++){
            if(i===-1 || j===-1 || i===rows || j===cols){
                out.add(`${i},${j}`);
            }
        }
    }
    
    let [r,c] = [0,0];
    let res = [];
    while(res.length < rows*cols){
        
        // Add new element to res, if it isn't already there
        if(!out.has(`${r},${c}`)){
            out.add(`${r},${c}`);
            res.push(matrix[r][c]);
        }
        
        // Set new coordinates, if they are out of bounds, set them back and rotate direction using modulo
        let newCoords = [r+dirs[dirIdx%4][0],c+dirs[dirIdx%4][1]];
        if(out.has(`${newCoords[0]},${newCoords[1]}`)){
            dirIdx++;
        } else {
            [r,c] = newCoords;
        }
        
    }
    
    return res;
};