/**
 * @param {Function[]} functions
 * @return {Function}
 */
var compose = function(functions) {
    return function(x){
        let res = x;
        for(let fn of functions.reverse()){
            res = fn(res)
        }
        return res;
    }
};

/**
 * const fn = compose([x => x + 1, x => 2 * x])
 * fn(4) // 9
 */