/**
 * @param {string} val
 * @return {Object}
 */
var expect = function(val) {
    // this.val = val;
    
    function toBe(comp){
        if(val!==comp) throw("Not Equal")
        return val===comp;
    }
    function notToBe(comp){
        if(val===comp) throw("Equal")
        
        return val!==comp;
    }
    return {toBe,notToBe}
};

/**
 * expect(5).toBe(5); // true
 * expect(5).notToBe(5); // throws "Equal"
 */