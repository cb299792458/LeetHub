function convert(s, numRows) {
    function row(index){
        let cycle = 2*numRows-2 || 1;
        let cycleIdx = index%cycle;
        if(cycleIdx<numRows) return cycleIdx
        else return cycle-cycleIdx;
    }
    
    let rows = new Array(numRows).fill().map(() => new Array);
    for(let i=0;i<s.length;i++) rows[row(i)].push(s[i]);

    let ans = '';
    for(let r of rows) ans += r.join('')
    return ans
}