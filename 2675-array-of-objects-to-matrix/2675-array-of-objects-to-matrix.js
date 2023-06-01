/**
 * @param {Array} arr
 * @return {Matrix}
 */
var jsonToMatrix = function(arr) {
    let keys = new Set();
    
    function dfsKeys(prefix,obj){
        if(typeof obj !== 'object' || obj===null){
            keys.add(prefix);
            return;
        }
        for(let [key, val] of Object.entries(obj)){
            dfsKeys(prefix ? prefix+'.'+key : key, val); // fancy ternary to handle falsy prefix
        }
    }
    
    for(let line of arr) dfsKeys('',line)
    
    keys = Array.from(keys);
    keys.sort( (a,b) => a<b ? -1 : 1 ); // default sort works fine
    const res = new Array(arr.length+1).fill().map(()=>new Array(keys.length).fill('')); 
    res[0] = keys;
    console.log(res[0]) // now we can finally do the problem
    
    for(let r=1;r<res.length;r++){ // skip row 0, which is all keys
        let line = arr[r-1]; // need a -1 !!! b/c arr has one less row than res !!!
        for(let c=0;c<res[0].length;c++){
            let path = res[0][c];
            let steps = path.split('.');
            
            let current = line;
            try{
                let fail = false;
                for(let step of steps){
                    if(typeof current==='string') fail=true;
                    current = current[step];
                }
                
                // edge cases
                if(fail) continue;
                if(current===undefined) continue;
                if(typeof current === 'object' && current !== null) continue;
                
                res[r][c]=current;
                // console.log(`just set ${r},${c} to ${current}`)
            }
            catch(err){
                // do nothing;
            }
        }
    }
    return res;
};
