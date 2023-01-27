/**
 * @param {character[][]} board
 * @param {string} word
 * @return {boolean}
 */
var exist = function(board, word) {
    
    function search(word,row,col){
        if(!word) return true;
        if(row<0||row>=board.length) return false;
        if(col<0||col>=board[0].length) return false;
        
        if(board[row][col]!==word[0]) return false;
        let char = board[row][col]
        board[row][col] = ' '
        
        if(search(word.slice(1),row+1,col)) return true;
        if(search(word.slice(1),row-1,col)) return true;
        if(search(word.slice(1),row,col+1)) return true;
        if(search(word.slice(1),row,col-1)) return true;
        board[row][col] = char;
    }
    
    for(let i=0;i<board.length;i++){
        for(let j=0;j<board[0].length;j++){
            if(search(word,i,j)) return true;
        }
    }
    return false;
};