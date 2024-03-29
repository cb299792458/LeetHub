/**
 * @param {character[][]} board
 * @return {boolean}

make a dict for rows and a dict for cols
colDict[y] = new Set()         // create an array for each col

for each x:
    for each y:
        colDict[y].add(board[y][x]) // add the number to the array/set
one subgrid: x: 0,1,2 -> outer key
             y: 0,1,2 -> inner key

             x: 3,4,5 -> 
             y: 0,1,2

             x: 6,7,8 -> 
             y: 0,1,2


 */
var isValidSudoku = function(board) {
    let colDict = {0: new Set(), 1: new Set(), 2: new Set(), 3: new Set(), 4: new Set(), 5: new Set(), 6: new Set(), 7: new Set(), 8: new Set()};
    let rowDict = {0: new Set(), 1: new Set(), 2: new Set(), 3: new Set(), 4: new Set(), 5: new Set(), 6: new Set(), 7: new Set(), 8: new Set()};
    let subGridDict = {
        0: {0: new Set(), 1: new Set(), 2: new Set()},
        1: {0: new Set(), 1: new Set(), 2: new Set()},
        2: {0: new Set(), 1: new Set(), 2: new Set()},
    }

    for (let y = 0; y<board.length; y++) { // rows
        for (let x = 0; x<board[0].length; x++) { // cols
            if (colDict[x].has(board[y][x]) && board[y][x] !== '.') {
                return false
            }
            if (rowDict[y].has(board[y][x]) && board[y][x] !== '.') {
                return false
            }

            // cols
            colDict[x].add(board[y][x])

            // rows
            rowDict[y].add(board[y][x])

            const outerKey = Math.floor(x/3)
            const innerKey = Math.floor(y/3)

            if ( subGridDict[outerKey][innerKey].has(board[y][x]) && board[y][x] !== '.' ) {
                return false
            }

            subGridDict[outerKey][innerKey].add(board[y][x])
        }
    }
    return true
};