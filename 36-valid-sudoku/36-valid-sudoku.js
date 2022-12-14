/**
 * @param {character[][]} board
 * @return {boolean}
 */
var isValidSudoku = function(board) {
    let rows = new Map();
    let cols = new Map();
    let boxs = new Map();
    
    for(let i=0; i<9; i++){
        for(let j=0; j<9; j++){
            
            if(!rows[i]){rows[i] = new Set();}
            if(!cols[j]){cols[j] = new Set();}
            if(!boxs[[Math.floor(i/3),Math.floor(j/3)]]){boxs[[Math.floor(i/3),Math.floor(j/3)]] = new Set();}
            
            if(rows[i].has(board[i][j])){
                return false;
            } else if(board[i][j] !== '.'){
                rows[i].add(board[i][j]);
            }
            
            if(cols[j].has(board[i][j])){
                return false;
            } else if(board[i][j] !== '.'){
                cols[j].add(board[i][j]);
            }
            
            if(boxs[[Math.floor(i/3),Math.floor(j/3)]].has(board[i][j])){
                return false;
            } else if(board[i][j] !== '.'){
                boxs[[Math.floor(i/3),Math.floor(j/3)]].add(board[i][j]);
            }
            console.log(boxs)
        }
    }

    return true;
};