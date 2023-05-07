/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    let num = init;
    function inc(){
        num++;
        return num;
    }
    function dec(){
        num--;
        return num;
    }
    function res(){
        num=init;
        return num;
    }
    return {increment: inc, decrement: dec, reset: res}
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */