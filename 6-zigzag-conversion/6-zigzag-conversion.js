/**
 * @param {string} s
 * @param {number} numRows
 * @return {string}
 */
var convert = function(s, numRows) {
    let goingDown = true;
    let arr = new Array(numRows);
    for(let j=0; j<numRows; j++ ) {
        arr[j] = [];
    }
    let i = 0;
    console.log(arr);
    s.split('').forEach( (char) => {
        arr[i].push(char); 
        if(i===0){goingDown = true}
        if(i===numRows-1){goingDown = false}
        if(numRows === 1){}
        else{
            if(goingDown){i++} else {i--}
        }
    });
    
    let ans = '';
    arr.forEach((sub) =>{
        sub.forEach((char) =>{
            ans += char;
        })
    })
    return ans;
};