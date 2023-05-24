/**
 * @param {any} o1
 * @param {any} o2
 * @return {boolean}
 */
var areDeeplyEqual = function(o1, o2) {
    
    const [t1,t2] = [typeof o1, typeof o2]
    if (t1!==t2) return false;
    if(Array.isArray(o1)!==Array.isArray(o2)) return false;
    
    if(t1==='object' && o1 !== null){
        
        const [k1,k2] = [Object.keys(o1), Object.keys(o2)]
        if (k1.length!==k2.length) return false;

        for(let key of k1){
            if(!areDeeplyEqual(o1[key],o2[key])) return false;
        }
    
    } else {
        return o1===o2;
    }
    
    return true;
};